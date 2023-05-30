Created: 2023-05-26 16:34
#paper
## Main idea
The paper tackles the problem of domain specific data augmentation for MT. 
For professional translations, the preservation of the domain knowledge from the source to the target is crucial, but it is sometime difficult to have parallel in-domain data.
To deal with this, this work propose a way to generate domain specific text that can be used for machine translations in two situations:
1. simulation of a small bilingual dataset;
2. simulation of the monolingual source text to be translated

Pre-trained LMs are used in both cases.
Combining these the approach presented with back translation can lead to the generation of very big synthetic bilingual in-domain data.
Mixed fine-tuning of [[Transformer]]-based models achieve SOTA results.

## Results
The approaches are tested on Arabic-to-English and English-to-Arabic generic datasets, collected from OPUS. 
Several metrics were used, like spBLEU, chrF++, TER, and COMET. Then human evaluation was also performed.
Significant improvements are reported for both approaches  in every metric (except for TER).

For the Arabic-to-English language direction, human evaluation demonstrates that Case 2 is on par with Case 1 even though in the former we did not have any authentic bilingual in-domain data. Nevertheless, the English-to-Arabic model in Case 2 has lower performance compared to the Case 1 model, although both setups outperform the baseline on the in-domain test set. The authors believe this might be due to the quality of synthetic data generated for Arabic, which is an interesting aspect to explore further.

## Ideas for future works:
- Utilize terminology for domain-specific data generation;
- use these approaches for low-resource languages and multilingual settings

## In deep
The paper investigate two scenarios of in-domain data scarcity.

### Case 1: Limited bilingual in-domain data available
This scenario happens when there is a large bilingual generic dataset but the bilingual in-domain dataset is not enough to fine-tune a baseline.
Approach:
1. use [[Large Language Models (LLMs)]] in the target language to augment the in-domain data. Each target sentence is used in a prompt to generate synthetic segments;
2. back-translation to the source language;
3. mixed fine-tuning on the baseline model. That means that the model is trained on a mix of synthetic bilingual in-domain dataset and a randomly sampled subset of the original generic dataset (ratio 1:9). To apply oversampling the datasets are weighted in different ways (0.9 for the synthetic data and 0.1 for the original one)
4. translations on in-domain data are much better, but on generic data there is a downgrade -> checkpoint average can reduce variability between trainings and address rapid overfitting during fine-tuning.

### Case 2: Zero bilingual in-domain data available
In this scenario there is a total absence of bilingual in-domain data.
Before applying the steps listed in the previous case, use the baseline MT model for forward-translation of the source-text. These translations are not going to be perfect but still they will include useful information about the domain.

### Models and datasets
Several stages of filtering were performed on the datasets (rule-based to remove duplicates HTML tags, and so on, semantic filtering to remove couples with similarity under a threshold, and then global filtering).
For in-domain NMT models, TICO-19 (which is about Public Health) was used.
Vocabulary is obtained by using SentencePiece model.
The baseline NMT model used is OpenNMT-tf.
For data generation, GPT-J and mGPT are used for English and Arabic, respectively.
For back-translation OPUS models were used.

The baseline model is firstly trained on the out-of-domain data and then fine-tuned on a mix of in-domain and out-of-domain data. Out-of-domain data samples used during the second fine-tuning are taken randomly.

## References
1. [Paper](https://aclanthology.org/2022.amta-research.2.pdf)

## Code
1. [GitHub](https://github.com/ymoslem/MT-LM)

## Tags
#nmt #machinetranslation 