import dataset
import time

from statistics import mean, stdev
from collections import Counter
from functools import reduce

import pandas as pd
import numpy as np

import gensim

import re
import emoji

import multiprocessing

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.cluster import KMeans

from kneed import KneeLocator


# Geonames dataset (https://www.geonames.org/export/)
dataset_geonames = pd.DataFrame(
    columns=['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude',
             'feature class', 'feature code', 'country code', 'cc2',
             'admin1 code', 'admin2 code', 'admin3 code', 'admin4 code',
             'population', 'elevation', 'dem', 'timezone', 'modification date'])


def parallelize_dataframe(df, func, n_cores=multiprocessing.cpu_count() - 1):
    """
    Horizontally split the dataframe based on the number of cores available in the system and apply the given function
    on each of the separate parts in parallel.

    :param df: the dataframe to use.
    :param func: the function to apply.
    :param n_cores: the number of cores to use.
    :return: the resulting dataframe.
    """
    df_split = np.array_split(df, n_cores)
    pool = multiprocessing.Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df


def z_score(df, column):
    """
    Apply the z-score method in Pandas using the .mean() and .std() method on the provided dataframe for the given
    column. The computed z-score will be introduced into a new column named by the original column along with the
    suffix '_norm'.

    **CANNOT BE EXECUTED IN PARALLEL** (due to computation of mean/std over all sets)

    :param df: the dataframe to use.
    :param column: the column to apply the z-score.
    :return: the resulting dataframe.
    """
    # copy the dataframe
    df_std = df.copy()
    # apply the z-score method
    df_std[column + '_norm'] = (df_std[column] - df_std[column].mean()) / df_std[column].std()

    return df_std


def demojize(field):
    try:
        result = emoji.demojize(field)

    except:
        result = field

    return result


def preprocess_dataset(dataset_local, categories='categories', description='description', duration='duration',
                       creationDate='creationDate', lastUpdate='lastUpdate', datePublishing='datePublishing',
                       feature='feature', imageId='imageId', videoId='videoId', versionHistory='versionHistory',
                       title='title'):
    """
    Preprocess certain columns of the dataset:
    (1) fill in missing vaues.
    (2) Look into the description column and (a) convert any emoji icons into words, (b) compute the length of the
    description (in characters), (c) extract all hashtags included in the description.
    (3) convert the duration from ms to minutes.
    (4) compute the age of each row in number of days from today.

    :param dataset_local: the dataframe to use.
    :param categories: the column name where the categories are stored.
    :param description: the column name where the description is stored.
    :param duration: the column name where the duration is stored.
    :param creationDate: the column name where the creation Date is stored.
    :param lastUpdate: the column name where the last update Date is stored.
    :param datePublishing: the column name where the publish Date is stored.
    :param feature: the column name where the features are stored.
    :param imageId: the column name where the imageId is stored.
    :param videoId: the column name where the videoId is stored.
    :param versionHistory: the column name where the version history is stored.
    :param title: the column name where the title is stored.
    :return: the resulting dataframe.
    """

    # Fill in missing values
    dataset_local[categories] = dataset_local[categories].apply(lambda d: d if isinstance(d, list) else [])
    dataset_local[feature] = dataset_local[feature].apply(lambda d: d if isinstance(d, list) else [])
    dataset_local[duration].fillna(0, inplace=True)
    dataset_local[imageId].fillna('', inplace=True)
    dataset_local[videoId].fillna('', inplace=True)
    dataset_local[description].fillna('', inplace=True)
    dataset_local[lastUpdate].fillna(pd.to_datetime("now").tz_localize('UTC'), inplace=True)
    dataset_local[datePublishing].fillna(pd.to_datetime("now").tz_localize('UTC'), inplace=True)
    dataset_local[creationDate].fillna(pd.to_datetime("now").tz_localize('UTC'), inplace=True)
    dataset_local[versionHistory] = dataset_local[versionHistory].apply(lambda d: d if isinstance(d, list) else [])

    # Convert Emoji into word descriptions
    dataset_local['description_noemoji'] = dataset_local.apply(lambda row: demojize(row[description]), axis=1)
    dataset_local['title_clean'] = dataset_local.apply(lambda row: demojize(row[title]), axis=1)

    # Extract hashtags
    pat = re.compile(r"#(\w+)")
    dataset_local['hashtags'] = dataset_local.apply(
        lambda row: list(set(dataset.pat_hashtags.findall(row['description_noemoji'].lower()))),
        axis=1)

    # Remove Hashtags from description
    dataset_local['description_clean'] = dataset_local.apply(
        lambda row: dataset.remove_hashtags(row['description_noemoji']),
        axis=1)

    # Remove Verbs from description
    dataset_local['description_noverbs'] = dataset_local.apply(
        lambda row: dataset.remove_verbs(row['description_noemoji']),
        axis=1)

    # Convert text to words and remove punctuations, too small/big words and stop words
    dataset_local['description_words'] = dataset_local.apply(
        lambda row: [word for word in gensim.utils.simple_preprocess(str(row['description_noverbs']), deacc=True)],
        axis=1)

    dataset_local['title_words'] = dataset_local.apply(
        lambda row: [word for word in gensim.utils.simple_preprocess(str(row['title_clean']), deacc=True)],
        axis=1)

    # Identify Location Names
    dataset_local['landmarks'] = dataset_local.apply(
        lambda row: dataset.identify_landmarks(row['description_clean'], dataset_geonames),
        axis=1)

    dataset_local['landmarks_title'] = dataset_local.apply(
        lambda row: dataset.identify_landmarks(row['title_clean'], dataset_geonames),
        axis=1)

    # Compute description and title length in characters (including white spaces)
    dataset_local['description_len'] = dataset_local.apply(lambda row: len(row['description_clean']), axis=1)
    dataset_local['title_len'] = dataset_local.apply(lambda row: len(row['title_clean']), axis=1)

    # Convert duration from ms to minutes
    dataset_local['duration_min'] = dataset_local.apply(lambda row: row[duration] / 60000, axis=1)

    # Compute age of entry in days from today
    dataset_local['days'] = 0
    dataset_local.days = (pd.to_datetime("now").tz_localize('UTC') - pd.to_datetime(
        dataset_local[creationDate])) // np.timedelta64(1, 'D')

    return dataset_local


def extract_ngrams(dataset_local):
    """
    Construct bi-gram and tri-gram model based on entire corpus and use it to identify n-grams in descriptions.
    1. Starting from the description, replace emojis using demojize function
    2. Remove hashtags
    3. Remove verbs + auxiliary verbs.
    4. Gensim simple preprocessing that removes punctuations, too small/big words and stop words.
    5. Identify bi-grams and tri-grams based on gensim.models.Phrases.

    :param dataset_local: the dataframe to use.
    :return: the resulting dataset.
    """
    bigram = gensim.models.Phrases(dataset_local['description_words'], min_count=5, threshold=30,
                                   connector_words=frozenset(dataset.it_common_terms))

    trigram = gensim.models.Phrases(bigram[dataset_local['description_words']], min_count=1, threshold=10,
                                    connector_words=frozenset(dataset.it_common_terms))

    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    dataset_local['description_ngrams'] = dataset_local.apply(
        lambda row: trigram_mod[bigram_mod[row['description_words']]],
        axis=1)

    return dataset_local


def extract_categories(dataset_local, categories='categories'):
    """
    Collect all the categories used in the dataset and hot-encode them.
    **CANNOT BE EXECUTED IN PARALLEL**

    :param df: the dataframe to use.
    :param categories: the column name where the categories are stored.
    :return: the resulting dataset.
    """
    counter = Counter(
        reduce(lambda x, y: x + y, dataset_local[(dataset_local[categories].isnull() == False)].categories))

    categories_found = list(counter.keys())

    # hot-encode emotions
    for category in categories_found:
        dataset_local['category_' + category.replace(' ', '_')] = 0
        dataset_local['category_' + category.replace(' ', '_')] = dataset_local[
            (dataset_local[categories].isnull() == False)].apply(
            lambda row: 1 if category in row[categories] else 0, axis=1)

    return dataset_local


def extract_hashtags(dataset_local, categories='hashtags'):
    """
    Collect all the hashtags used in the dataset and hot-encode them.
    **CANNOT BE EXECUTED IN PARALLEL**

    :param df: the dataframe to use.
    :param hashtags: the column name where the hashtags are stored.
    :return: the resulting dataset.
    """
    counter = Counter(
        reduce(lambda x, y: x + y, dataset_local[(dataset_local['hashtags'].isnull() == False)].hashtags))

    hashtags_found = list(counter.keys())

    # hot-encode emotions
    for hashtag in hashtags_found:
        dataset_local['hashtag_' + hashtag.replace(' ', '_')] = 0
        dataset_local['hashtag_' + hashtag.replace(' ', '_')] = dataset_local[
            (dataset_local['hashtags'].isnull() == False)].apply(
            lambda row: 1 if hashtag in row['hashtags'] else 0, axis=1)

    return dataset_local


def update_ngrams(dataset_local, description='description_clean',
                  description_ngrams='description_ngrams'):
    """
    Replace the words with their bigrams and trigrams.
    1. We start from the clean description (without hashtags and with converted emojis)
    2. Replace all occurance of bigrams and trigrams

    :param dataset_local: the dataframe to use.
    :param description: the column name where the description is stored.
    :param description_ngrams: the column name where the ngrams are stored.
    :return: the resulting dataset.
    """
    dataset_local['ngrams'] = dataset_local.apply(
        lambda row: dataset.extract_ngrams(row[description_ngrams]),
        axis=1)

    dataset_local['description_with_ngrams'] = dataset_local.apply(
        lambda row: dataset.replace_ngrams(row[description], row[description_ngrams]),
        axis=1)

    return dataset_local


def extract_writing_style(dataset_local, description='description_with_ngrams',
                          title_words='title_words'):
    """
    Extract list words from description, excluding numbers, punctuation and stop words based on the Spacy library.
    Exclude common words (e.g., biglietti, tour, rome, etc).
    Extract stems from words based on the Spacy library.
    Identify unique words.
    Extract  adjectives and verbs using the Spacy Library based on part-of-speech (POS) tagging.
    Extract list of sentences.

    :param dataset_local: the dataframe to use.
    :param description: the column name where the description is stored.
    :param title_words: the column name where the processed title is stored.
    :return: the resulting dataframe.
    """
    dataset_local['title_words_list'] = dataset_local.apply(lambda row: dataset.process_words_aslist(row[title_words]),
                                                            axis=1)
    dataset_local['words_list'] = dataset_local.apply(lambda row: dataset.process_words(row[description]),
                                                      axis=1)
    dataset_local['words_set'] = dataset_local.apply(lambda row: set(row['words_list']), axis=1)

    dataset_local['entities'] = dataset_local.apply(lambda row: dataset.extract_entities(row[description]),
                                                    axis=1)
    dataset_local['adjectives'] = dataset_local.apply(
        lambda row: dataset.extract_by_position(row[description], ['ADJ']), axis=1)

    dataset_local['verbs'] = dataset_local.apply(lambda row: dataset.extract_by_position(row[description], ['VERB']),
                                                 axis=1)

    dataset_local['nouns'] = dataset_local.apply(lambda row: dataset.extract_by_position(row[description], ['NOUN']),
                                                 axis=1)

    dataset_local['propns'] = dataset_local.apply(lambda row: dataset.extract_by_position(row[description], ['PROPN']),
                                                  axis=1)

    dataset_local['sentences'] = dataset_local.apply(lambda row: dataset.extract_sentences(row[description]), axis=1)

    return dataset_local


def my_mean(list):
    if len(list) < 2:
        return list[0]
    else:
        return mean(list)


def my_stdev(list):
    if len(list) < 2:
        return 0
    else:
        return stdev(list)


def statistics_writing_style(dataset_local):
    """
    For each record, count the number of words, unique words, named entities, adjectives, verbs, sentences,
    mean number of words per sentence, stdev of words per sentence.

    :param dataset_local: the dataframe to use.
    :return: the resulting dataframe.
    """
    dataset_local['title_words_count'] = dataset_local.apply(lambda row: len(row['title_words_list']), axis=1)
    dataset_local['words_count'] = dataset_local.apply(lambda row: len(row['words_list']), axis=1)
    dataset_local['words_unique'] = dataset_local.apply(lambda row: len(row['words_set']), axis=1)
    dataset_local['landmarks_count'] = dataset_local.apply(lambda row: len(row['landmarks']), axis=1)
    dataset_local['entities_count'] = dataset_local.apply(lambda row: len(row['entities']), axis=1)
    dataset_local['adjectives_count'] = dataset_local.apply(lambda row: len(row['adjectives']), axis=1)
    dataset_local['verbs_count'] = dataset_local.apply(lambda row: len(row['verbs']), axis=1)
    dataset_local['nouns_count'] = dataset_local.apply(lambda row: len(row['nouns']), axis=1)
    dataset_local['propns_count'] = dataset_local.apply(lambda row: len(row['propns']), axis=1)
    dataset_local['ngrams_count'] = dataset_local.apply(lambda row: len(row['ngrams']), axis=1)
    dataset_local['hashtags_count'] = dataset_local.apply(lambda row: len(row['hashtags']), axis=1)
    dataset_local['sentences_count'] = dataset_local.apply(lambda row: len(row['sentences']), axis=1)
    dataset_local['sentences_mean_len'] = dataset_local.apply(
        lambda row: my_mean([len(sentence) for sentence in row['sentences']]), axis=1)
    dataset_local['sentences_mean_words'] = dataset_local.apply(
        lambda row: my_mean([len(dataset.process_words(sentence)) for sentence in row['sentences']]), axis=1)
    dataset_local['sentences_stdev_words'] = dataset_local.apply(
        lambda row: my_stdev([len(dataset.process_words(sentence)) for sentence in row['sentences']]), axis=1)

    return dataset_local


def analysis_tfidf(dataset_with_features,
                   column: str,
                   min_df:int = 3,
                   max_df:int = 0.25):
    """
    Carry out a TF-IDF analysis on the column provided.

    :param dataset_with_features: the dataframe to use that contains the extracted features.
    :param column: the column name where the values that will be used for the analysis are found.
    :param min_df: When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold. This value is also called cut-off in the literature. If float in range of [0.0, 1.0], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.
    :param max_df: When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words). If float in range [0.0, 1.0], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.
    :return: the resulting dataframe.
    """
    tfidf_text_vector = TfidfVectorizer(input='content',
                                        tokenizer=lambda text: text,
                                        lowercase=False,
                                        min_df=min_df,
                                        max_df=max_df)
    result_text = tfidf_text_vector.fit_transform(dataset_with_features[column])
    dense_text = result_text.todense()
    denselist_text = dense_text.tolist()

    dataset_text_tfidf = pd.DataFrame(denselist_text, index=dataset_with_features.index,
                                      columns=tfidf_text_vector.get_feature_names())

    return dataset_text_tfidf


def identify_bestfeatures(dataset_text_tfidf,
                          n_clusters: int,
                          top_features: int = 50,
                          min_score: int = 10,
                          random_state: int = 42):
    """
    Identify the best features based on the SelectKBest method and chi2 test.

    :param dataset_text_tfidf: the dataframe to use - resulting from the tfidf analysis.
    :param n_clusters: the number of clusters to use.
    :param top_features: the number of top features to consider.
    :param min_score: the minimum score the features need to have.
    :return: the resulting dataframe.
    """
    model = KMeans(n_clusters, init='k-means++', random_state=random_state)
    model.fit(dataset_text_tfidf)
    labels = model.labels_

    bestfeatures = SelectKBest(chi2, k=top_features)
    fit_data = bestfeatures.fit(dataset_text_tfidf, labels)

    dfscores = pd.DataFrame(fit_data.scores_)
    dfcolumns = pd.DataFrame(dataset_text_tfidf.columns)
    featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    featureScores.columns = ['Specs', 'Score']

    return featureScores[featureScores.Score > min_score]


def clusterdata(dataset_text_tfidf,
                n_clusters: int,
                random_state: int = 42):
    """
    Cluster data using K-means++.

    :param dataset_text_tfidf: the dataframe to use - resulting from the tfidf analysis.
    :param n_clusters: the number of clusters to use.
    :return: the resulting labels.
    """
    model = KMeans(n_clusters, init='k-means++', random_state=random_state)
    model.fit(dataset_text_tfidf)
    labels = model.labels_

    return labels


def locate_cluster_knee_point(dataset,
                              min_clusters:int = 1,
                              max_clusters:int = 20,
                              random_state: int = 42) -> int:
    """
    Use Knee point detection algorithm to identify optimal number of clusters for K-means++.

    :param dataset: the data to use for the clustering.
    :param min_clusters: Minimum number of clusters to examine.
    :param max_clusters: Maximum number of clusters to examine.

    :return: the optimal number of clusters.
    """
    sse = {}

    for k in range(min_clusters, max_clusters):
        kmeans = KMeans(n_clusters=k, random_state=random_state)
        kmeans.fit(dataset)
        sse[k] = kmeans.inertia_

    kn = KneeLocator(x=list(sse.keys()),
                 y=list(sse.values()),
                 curve='convex',
                 direction='decreasing')

    return kn.knee


def perform_clustering(dataset_local,
                       column: str,
                       n_clusters: int = -1,
                       min_df: int = 3,
                       max_df: int = 0.25,
                       top_features: int = 50,
                       min_score: int = 10,
                       random_state: int = 42):
    """
    Cluster data using K-means++ based on the TF-IDF analysis and the identification of the k-best features.

    :param dataset_local: the dataframe to use.
    :param n_clusters: the number of clusters to use.
    :param column: the column name where the values that will be used for the analysis are found.
    :param min_df: When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold. This value is also called cut-off in the literature. If float in range of [0.0, 1.0], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.
    :param max_df: When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words). If float in range [0.0, 1.0], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.
    :param top_features: the number of top features to consider.
    :param min_score: the minimum score the features need to have.

    :return: the resulting dataframe with the labels.
    """
    dataset_text_tfidf = analysis_tfidf(dataset_local, column, min_df, max_df)

    # Check if we need to identify number of clusters using the Elbow Method
    if n_clusters == -1 :
        cluster_size = locate_cluster_knee_point(dataset_text_tfidf)
    else:
        cluster_size = n_clusters

    best_features = identify_bestfeatures(dataset_text_tfidf, cluster_size, top_features, min_score)
    labels = clusterdata(dataset_text_tfidf[list(best_features.Specs)], cluster_size)
    dataset_local['cluster_' + column] = labels

    return dataset_local


def statistics_sentiments(dataset_local):
    """
    For each record compute the compound sentiment and hot-encode the count of positive and negative sentences.

    :param dataset_local: the dataframe to use.
    :return: the resulting dataframe.
    """
    dataset_local['sentiment_dict'] = dataset_local.apply(lambda row: dataset.merge_into_dict(row['sentiment']), axis=1)
    dataset_local['sentiment_compound'] = dataset_local.apply(
        lambda row: dataset.compute_compound(row['sentiment_dict']), axis=1)

    sentiments = ['positive', 'negative']

    # hot-encode emotions
    for sentiment in sentiments:
        dataset_local['sentiment_' + sentiment] = 0
        dataset_local['sentiment_' + sentiment] = dataset_local.apply(
            lambda row: row['sentiment_dict'][sentiment] if sentiment in row['sentiment_dict'] else 0, axis=1)

    return dataset_local


def statistics_emotions(dataset_local):
    """
    Count the emotions of each sentence and hot encode them as separate columns.

    :param dataset_local: the dataframe to use.
    :return: the resulting dataframe.
    """
    dataset_local['emotion_dict'] = dataset_local.apply(lambda row: dataset.merge_into_dict(row['emotion']), axis=1)

    emotions = ['joy', 'sadness', 'anger', 'fear']

    # hot-encode emotions
    for emotion in emotions:
        dataset_local['emotion_' + emotion] = 0
        dataset_local['emotion_' + emotion] = dataset_local.apply(
            lambda row: row['emotion_dict'][emotion] if emotion in row['emotion_dict'] else 0, axis=1)

    return dataset_local


def normalize_statistics(dataset_local, columns):
    """
    Normalize a given set of columns using the min/max scaller method.

    :param dataset_local: the dataframe to use.
    :param columns: The columns to normalize.
    :return: the resulting dataframe.
    """
    for column in columns:
        dataset_local[column + '_norm'] = (dataset_local[column] - dataset_local[column].min()) / (
                dataset_local[column].max() - dataset_local[column].min())

    return dataset_local


def analyze_dataset(filename, outfile, geonames):
    """
    Fill in missing values, preprocess and extract the following features from the dataset:

    Basic Features:
     * Owner (author)
     * Location
     * Landmarks
      * Number of Landmarks
     * Unique Named Entities (from part-of-speech tagging)
      * Number of unique named entities
     * Categories
      * Hot-encode categories
     * Hashtags
     * Duration
     * Age (in days)

    Writing Style Features:
     * Description Length
     * Title Length
     * All words used
      * Number of words used
     * Unique Words
      * Number of unique words
     * Unique Verbs
      * Number of unique verbs
     * Unique Adjectives
      * Number of unique adjectives
     * List of sentences
      * Number of sentences
      * Mean number of words per sentence
      * Stdev of words per sentence

    Clustering based on Features:
     * Nouns, Verbs, Named Entities, Adjectives

    Sentiment and Emotion Features:
     * Sentiment of each sentence
      * Hot-encode emotions
      * Compound Sentiment
     * Emotions of each sentence
      * Hot-encode emotions

    :param filename: the dataset in json format.
    :param outfile: the resulting dataset in pickle format.
    :param geonames: the geoname datasets to consider when searching landmarks.
    """
    print('CPU cores available: ', multiprocessing.cpu_count())

    print(f'Loading geoname datasets', end='')
    t = time.perf_counter()
    global dataset_geonames
    dataset_geonames = dataset.load_geonames(geonames)
    total = time.perf_counter() - t
    print(f' found ' + str(len(dataset_geonames)) + ' entries', end='')
    print(f' {total:.4f} sec')

    print(f'Reading {filename}', end='')
    t = time.perf_counter()
    dataset_easytour = pd.read_json(filename, convert_dates=['creationDate', 'lastUpdate', 'datePublishing'])
    total = time.perf_counter() - t
    print(f' found ' + str(len(dataset_easytour)) + ' entries', end='')
    print(f' {total:.4f} sec')

    # Feature Extraction
    # -------------------------------------------------------------------------

    print('Preprosessing dataset', end='')
    t = time.perf_counter()
    dataset_easytour = parallelize_dataframe(dataset_easytour, preprocess_dataset)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    # Delete records with short description
    print('Deleting records with short description (less than 50), total: ',
          len(dataset_easytour[dataset_easytour.description_len <= 50]))
    dataset_easytour = dataset_easytour[dataset_easytour.description_len > 50]

    dataset_easytour.to_pickle(outfile)

    # Create bi-grams and tri-grams models
    print('Extract Bi-grams and Tri-grams', end='')
    t = time.perf_counter()
    dataset_easytour = extract_ngrams(dataset_easytour)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    print('Replacing bi-grams and tri-grams', end='')
    t = time.perf_counter()
    dataset_easytour = parallelize_dataframe(dataset_easytour, update_ngrams)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    print('Extracting categories used', end='')
    t = time.perf_counter()
    dataset_easytour = extract_categories(dataset_easytour)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    print('Extracting hashtags used', end='')
    t = time.perf_counter()
    dataset_easytour = extract_hashtags(dataset_easytour)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    print('Extracting writing style', end='')
    t = time.perf_counter()
    dataset_easytour = parallelize_dataframe(dataset_easytour, extract_writing_style)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    print('Producing statistics on writing style', end='')
    t = time.perf_counter()
    dataset_easytour = parallelize_dataframe(dataset_easytour, statistics_writing_style)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    dataset_easytour.to_pickle(outfile)

    # Clustering
    # -------------------------------------------------------------------------
    print('Clustering based on Nouns, Verbs, Named Entities, Adjectives, Pronouns', end='')
    t = time.perf_counter()
    for column in ['nouns', 'verbs', 'adjectives', 'entities', 'propns']:
        dataset_easytour = perform_clustering(dataset_easytour, column)

    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    dataset_easytour.to_pickle(outfile)

    # Sentiment & Emotion
    #-------------------------------------------------------------------------
    print('Extracting sentiments', end='')
    t = time.perf_counter()
    dataset_easytour['sentiment'] = dataset_easytour.apply(lambda row: dataset.extract_sentiment(row['description']),
                                                           axis=1)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    dataset_easytour.to_pickle(outfile)

    print('Produce statistics on sentiments', end='')
    t = time.perf_counter()
    dataset_easytour = parallelize_dataframe(dataset_easytour, statistics_sentiments)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    dataset_easytour.to_pickle(outfile)

    print('Extracting emotions', end='')
    t = time.perf_counter()
    dataset_easytour['emotion'] = dataset_easytour.apply(lambda row: dataset.extract_emotion(row['description']),
                                                         axis=1)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    dataset_easytour.to_pickle(outfile)

    print('Produce statistics on emotions', end='')
    t = time.perf_counter()
    dataset_easytour = parallelize_dataframe(dataset_easytour, statistics_emotions)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    dataset_easytour.to_pickle(outfile)

    # Columns that contain statistics that we need to normalize using z-score function.
    columns = ['duration', 'description_len', 'words_count', 'words_unique', 'entities_count', 'adjectives_count',
               'verbs_count', 'nouns_count', 'propns_count', 'ngrams_count', 'title_words_count', 'hashtags_count',
               'sentences_count', 'sentences_mean_words', 'sentences_stdev_words',
               'sentiment_compound', 'sentiment_positive', 'sentiment_negative',
               'emotion_joy', 'emotion_sadness', 'emotion_anger', 'emotion_fear']

    print('Normalizing statistics', end='')
    t = time.perf_counter()
    dataset_easytour = normalize_statistics(dataset_easytour, columns)
    total = time.perf_counter() - t
    print(f' {total:.4f} sec')

    print(f'Writing {outfile}')
    dataset_easytour.to_pickle(outfile)
