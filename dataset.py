from os import linesep
from tqdm import tqdm
import json
import itertools
import math
import string
import re
import pgeocode
import traceback
import spacy

import nltk
from nltk.util import ngrams
from nltk.stem import PorterStemmer

from feel_it import EmotionClassifier, SentimentClassifier

import pandas as pd

from gensim.utils import simple_preprocess

nomi = pgeocode.Nominatim('it')

nlp = spacy.load("it_core_news_lg")

it_common_terms = ['a',
                   'ad',
                   'al',
                   'allo',
                   'ai',
                   'agli',
                   'all',
                   'agl',
                   'alla',
                   'alle',
                   'con',
                   'col',
                   'coi',
                   'da',
                   'dal',
                   'dallo',
                   'dai',
                   'dagli',
                   'dall',
                   'dagl',
                   'dalla',
                   'dalle',
                   'di',
                   'del',
                   'dello',
                   'dei',
                   'degli',
                   'dell',
                   'degl',
                   'della',
                   'delle',
                   'gli',
                   'il',
                   'in',
                   'la',
                   'lo',
                   'nel',
                   'nello',
                   'nei',
                   'negli',
                   'nell',
                   'negl',
                   'nella',
                   'nelle',
                   'su',
                   'sul',
                   'sullo',
                   'sui',
                   'sugli',
                   'sull',
                   'sugl',
                   'sulla',
                   'sulle']

ps = PorterStemmer()

emotional_classifier = EmotionClassifier()
sentiment_classifier = SentimentClassifier()

pat_hashtags = re.compile(r"#(\w+)")

prefix_list = ['san', 'monte', 'piazza\sdel', 'piazza\sdi', 'piazza']
pat_landmarks = re.compile(r'(%s)\s(\w+)' % '|'.join(prefix_list))


def fix_duration(field):
    minutes = 0
    if 'hours' in field:
        text = field[0:field.find(' ')]
        if '-' in text:
            text = field[0:field.find('-')]

        if '–' in text:
            text = field[0:field.find('–')]

        if '+' in text:
            text = field[0:field.find('+')]

        hours = int(text)
        minutes = hours * 60

        if '-' in text or '–' in text:
            minutes += 30

    elif 'minutes' in field:
        text = field[0:field.find(' ')]
        if '-' in text:
            text = field[0:field.find('-')]

        minutes = int(text)

    elif 'Durata' in field:
        text = field[field.find(' '):]
        if 'h' in text:
            minutes = 0
            if len(text[text.find('h') + 1:]) > 0:
                minutes = int(text[text.find('h') + 1:-1])

            text = text[0:text.find('h')]
            hours = int(text)
            minutes += hours * 60

    return minutes


def load_dataset(entries_raw, unique_titles, empty, address_missing, address_missing_activities, address_dict,
                 filenames, dataset_path):
    for file in tqdm(filenames):
        if 'html' != file[-4:]:
            continue

        path = dataset_path + '/' + file
        f = open(path, "r")
        dic = f.read()
        f.close()
        try:
            dic = json.loads(dic)
        except:
            empty.append(path)

        try:
            # Skip empty records
            if 'title' not in dic or len(dic['title']) < 1:
                empty.append(path)
                continue

            if 'Languages' not in dic:
                empty.append(path)
                continue

            # extract duration from time
            duration = ''
            if 'time' in dic and len(dic['time']) > 0:
                duration = dic['time']

            elif 'duration' in dic and len(dic['duration']) > 0:
                duration = dic['duration']

            else:
                # sometimes duration is mixed in Languages
                contains = False
                for entry in dic['Languages']:
                    if 'ora' in entry:
                        contains = True
                        duration = entry
                        break

            # convert duration description to minutes
            duration_int = fix_duration(duration)

            # extract description
            description = ''
            if 'text' in dic and 'about' in dic:
                description = dic['about'] + dic['text']

            elif 'about' in dic:
                description = dic['about']

            elif 'text' in dic:
                description = dic['text']

            # extract location
            city = ''
            postcode = ''
            lat = ''
            long = ''

            if 'address' in dic:
                if 'addressLocality' in dic['address']:
                    city = dic['address']['addressLocality']
                elif 'addressRegion' in dic['address']:
                    city = dic['address']['addressRegion']

                if 'postalcode' in dic['address'] and len(dic['address']['postalcode']) > 0:
                    postcode = dic['address']['postalcode']

                elif 'postalCode' in dic['address'] and len(dic['address']['postalCode']) > 0:
                    postcode = dic['address']['postalCode']

                else:
                    if 'streetAddress' in dic['address'] and dic['address']['streetAddress'] in address_dict and len(
                            address_dict[dic['address']['streetAddress']]) > 0:
                        postcode = address_dict[dic['address']['streetAddress']]['postcode']
                        lat = address_dict[dic['address']['streetAddress']]['latitude']
                        long = address_dict[dic['address']['streetAddress']]['longitude']

                    else:
                        if 'streetAddress' in dic['address']:
                            address_missing.add(dic['address']['streetAddress'])

                        if 'addressLocality' in dic['address']:
                            postcode = dic['address']['addressLocality']

            elif 'Places' in dic and len(dic['Places']) > 0:
                contains = False
                for entry in dic['Places']:
                    if entry['Title'] in address_dict and len(address_dict[entry['Title']]) > 0:
                        contains = True
                        postcode = address_dict[entry['Title']]['postcode']
                        lat = address_dict[entry['Title']]['latitude']
                        long = address_dict[entry['Title']]['longitude']
                        break
                    else:
                        address_missing.add(entry['Title'])

            if city == '' and 'city' in dic:
                city = dic['city']

            if city == '' and len(postcode) > 0:
                city = nomi.query_postal_code(postcode).county_name

            if postcode == '':
                address_missing_activities.append(path)

            if dic['url'] not in unique_titles:
                unique_titles.add(dic['url'])

                # append new entry
                entries_raw['title'].append(dic['title'])
                entries_raw['duration'].append(duration)
                entries_raw['duration_int'].append(duration_int)
                entries_raw['description'].append(description)
                entries_raw['url'].append(dic['url'])
                entries_raw['city'].append(city)
                entries_raw['postcode'].append(postcode)
                entries_raw['lat'].append(lat)
                entries_raw['long'].append(long)

        except:
            print(path)
            print(traceback.format_exc())


def remove_hashtags(field):
    """
    Remove hashtags and lineseps from the field.

    :param field: the field to examine.
    :return: the field without any hashtags and lineseps.
    """
    description = str(field).replace('\n', ' ').replace('description_end', ' ').strip().lower()

    # remove hashtags
    hashtags = list(set(pat_hashtags.findall(description)))
    hashtags = sorted(hashtags, key=lambda x: len(x), reverse=True)
    for hashtag in hashtags:
        description = description.replace('#' + hashtag, '')

    return description.replace('#', '').strip()


def replace_ngrams(field, words_with_ngrams):
    """
    Remove hashtags and lineseps from the field.

    :param field: the field to examine.
    :return: the field without any hashtags and lineseps.
    """
    description = str(field).replace('\n', ' ').strip().lower()

    ngrams = [word for word in words_with_ngrams if '_' in word]
    ngrams = sorted(ngrams, key=lambda x: len(x), reverse=True)
    for ngram in ngrams:
        description = description.replace(ngram.replace('_', ' '), ngram)

    return description


def extract_ngrams(field):
    """
    Remove hashtags and lineseps from the field.

    :param field: the field to examine.
    :return: the field without any hashtags and lineseps.
    """
    return [word for word in field if '_' in word]


def load_geonames(geonames):
    dataset_geonames = pd.DataFrame(
        columns=['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude',
                 'feature class', 'feature code', 'country code', 'cc2', 'name_words', 'word_count'])

    # Ignore columns
    # 'admin1 code', 'admin2 code', 'admin3 code', 'admin4 code',
    # 'population', 'elevation', 'dem', 'timezone', 'modification date'

    # create list of all datasets
    dataframes = [pd.DataFrame(
        columns=['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude',
                 'feature class', 'feature code', 'country code', 'cc2', 'name_words', 'word_count'])]

    # Load one by one and prepare concatenation
    for geoname in geonames:
        dataset_lang = pd.read_csv(geoname, sep='\t', header=None,
                                   names=['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude',
                                          'feature class', 'feature code', 'country code', 'cc2'],
                                   usecols=range(0, 10))

        dataset_lang.dropna(subset=['asciiname'], inplace=True)
        dataset_lang['name_words'] = dataset_lang.apply(lambda row: row['asciiname'].split(' '), axis=1)
        dataset_lang['word_count'] = dataset_lang.apply(lambda row: len(row['name_words']), axis=1)

        dataframes.append(dataset_lang)

    # Concatenate
    dataset_geonames = pd.concat(dataframes)

    # Set index
    dataset_geonames.set_index(keys=['geonameid'], inplace=True)

    return dataset_geonames


def identify_locations(field, n, dataset_geonames):
    """
    Identify geographical locations using ngrams and the geonames database.
    https://www.geonames.org/export/

    :param field: the field to examine.
    :param n: the degree of the ngrams.
    :return: a list of geographical locations spotted in the field along with all the geonameid identified.
    """
    tokens = [token for token in str(field).replace(',', ' ').split(' ') if token != '']
    output = list(ngrams(tokens, n))
    dataset_geonames_subset = dataset_geonames[dataset_geonames.word_count == n]
    return [(' '.join(token),
             list(dataset_geonames_subset[dataset_geonames_subset.name.str.lower() == (' '.join(token))].index))
            for token in output
            if len(dataset_geonames_subset[dataset_geonames_subset.name.str.lower() == (' '.join(token))]) > 0]


def identify_landmarks(field, dataset_geonames):
    text = field.translate(str.maketrans('', '', string.punctuation)).lower()
    landmark_name = set()
    locations = []

    # Identify locations based on geonames dataset
    # for n in range(1, 2):
    #      found = identify_locations(text, n, dataset_geonames)
    #      for new_location in found:
    #          if not new_location[0] in landmark_name:
    #              landmark_name.add(new_location[0])
    #              locations.append(new_location)

    # Identify location based on list of regular expressions
    # re_results = pat_landmarks.findall(text)
    # for token in re_results:
    #     new_location = (' '.join(token), [])
    #     if not new_location[0] in landmark_name:
    #         landmark_name.add(new_location[0])
    #         locations.append(new_location)

    return locations


def text_to_words(field):
    """
    Split text field it in list of tokens after removing too short tokens (less than 2 characters), too long tokens
    (more than 15 characters) and punctuations.

    :param field: the field to process.
    """
    for sentence in sentences:
        yield gensim.utils.simple_preprocess(str(sentence), deacc=True)  # deacc=True removes punctuations


def process_words(field, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """
    Use lemmatization to identify Nouns, Adjectives, Verbs and Adverbs.

    :param field: the field to convert into a list of words.
    :return: a list of words.
    """
    doc = nlp(field)
    return [token.lemma_ for token in doc if token.pos_ in allowed_postags and len(token.lemma_) > 3]


def process_words_aslist(field, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """
    Use lemmatization to identify Nouns, Adjectives, Verbs and Adverbs.

    :param field: the field to convert into a list of words.
    :return: a list of words.
    """
    doc = nlp(' '.join(field))
    return [token.lemma_ for token in doc if token.pos_ in allowed_postags and len(token.lemma_) > 3]


def clean_text_aslist(field):
    """
    Convert document into a list of words. Remove hashtags, stop words, punctuations, numbers, black listed words.
    Use stemming to identify root of words.

    :param field: the field to convert into a list of words.
    :return: a list of words.
    """
    description = remove_hashtags(field)

    token_list = []
    doc = nlp.tokenizer(description.replace("'", ' ').replace("’", ' ').lower())
    for token in doc:
        if not token.is_stop \
                and not token.is_punct \
                and not str(token) in it_common_terms \
                and not str(token).isdigit() \
                and not len(str(token).strip()) < 2:
            token_list.append(ps.stem(str(token)))

    return token_list


def clean_text_astokens(field):
    """
    Convert document into a list of words. Remove hashtags, stop words, punctuations, numbers, black listed words.
    Use stemming to identify root of words.

    :param field: the field to convert into a list of words.
    :return: a list of words.
    """

    return clean_text_aslist(field)


def clean_text_asset(field):
    """
    Convert document into a set of words. Remove hashtags, stop words, punctuations, numbers, black listed words.
    Use stemming to identify root of words.

    :param field: the field to convert into a list of words.
    :return: a set of words.
    """

    return set(clean_text_aslist(field))


def extract_entities(field):
    """
    Analyze document based on part of speech and extract named entities.
    Use lemmatization to identify the lemmas of words.

    :param field: the field to extract named entities.
    :return: a set of named entities.
    """
    description = str(field).lower()

    token_set = set()
    doc = nlp(description)
    for token in doc.ents:
        if len(str(token)) > 3:
            token_set.add(str(token))

    return token_set


def remove_verbs(field):
    """
    Analyze document based on part of speech and extract entities based on their position in the sentence.
    Use lemmatization to identify the lemmas of words.

    :param field: the field to extract the entities based on their position.
    :param position: the position of the entity in the sentence.
    :return: a set of entities extracted.
    """
    doc = nlp(field.lower())
    return [token.lemma_ for token in doc if token.pos_ not in ['VERB', 'AUX']]


def extract_by_position(field, position):
    """
    Analyze document based on part of speech and extract entities based on their position in the sentence.
    Use lemmatization to identify the lemmas of words.

    :param field: the field to extract the entities based on their position.
    :param position: the position of the entity in the sentence.
    :return: a set of entities extracted.
    """
    doc = nlp(field.lower())
    return [token.lemma_ for token in doc if token.pos_ in position and len(str(token.lemma_)) > 3]


def extract_sentences(field):
    sentences = []
    doc = nlp(field)
    assert doc.has_annotation("SENT_START")
    for sent in doc.sents:
        sentences.append(sent.text)

    return sentences


def extract_emotion(field):
    return emotional_classifier.predict(extract_sentences(field))


def extract_sentiment(field):
    return sentiment_classifier.predict(extract_sentences(field))


def merge_into_dict(field):
    value_dict = {}
    for value in field:
        if value in value_dict:
            value_dict[value] = value_dict[value] + 1

        else:
            value_dict[value] = 1

    return value_dict


def compute_compound(field):
    positive = 0
    if 'positive' in field:
        positive = field['positive']

    negative: int = 0
    if 'negative' in field:
        negative = field['negative']

    return positive - negative


def compute_idf(dataset, column):
    # union of all verbs
    union = [entry for entry in dataset[column]]
    merge = list(itertools.chain(*union))
    unique = set(merge)

    total_documents = len(dataset)
    idf_dict = {}
    idf_list = []

    for entry in unique:
        occurrences = dataset.apply(lambda row: entry in row[column], axis=1).value_counts()[True]
        idf_dict[entry] = math.log10(total_documents / (float(occurrences) + 1))
        idf_list.append((entry, math.log10(total_documents / (float(occurrences) + 1))))

    idf_list.sort(key=lambda x: x[1], reverse=True)

    return idf_dict, idf_list
