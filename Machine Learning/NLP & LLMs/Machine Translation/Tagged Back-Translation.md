Created: 2023-05-30 15:15
#note

This approach aims at augmenting the available parallel training data with synthetic data that represent the purpose of the model.
This is very helpful when training NMT models for low-resource languages, but also enriches datasets with specific linguistic features in rich-resource languages.

Assuming we want to train an English-to-Hindi NMT mode, the Tagged Back-Translation data augmentation technique depends on the following steps:

1. For an English-to-Hindi model, train another Hindi-to-English model (i.e. in the other direction), using publicly available data from [OPUS](https://opus.nlpl.eu/);
2. Select monolingual data in Hindi publicly available (e.g. at [OSCAR](https://oscar-corpus.com/)), which must have domains and linguistic features similar to the potential texts to be translated;
3. Use the Hindi-to-English model to create a synthetic dataset, by translating the Hindi monolingual data into English. Note here that only the English side (the source for EN-HI) is MTed while the Hindi side (the target for EN-HI) is human-generated text;
4. Consider using one of the available Quality Estimation tools such as [TransQuest](https://github.com/TharinduDR/TransQuest) (Ranasinghe et al., 2020) or [OpenKiwi](https://github.com/Unbabel/OpenKiwi) (Kepler et al., 2019) to filter out back-translations of low quality;
5. Add a special tag like `<BT>` to the start of the MTed segments;
6. Build the vocabulary on all the data, both the original and the synthetic datasets;
7. Augment the original English-to-Hindi training dataset with the synthetic dataset;
8. Train a new English-to-Hindi model using the dataset generated from the previous step.

## References
1. [Blog](https://blog.machinetranslation.io/low-resource-nmt/)

## Code
1. 