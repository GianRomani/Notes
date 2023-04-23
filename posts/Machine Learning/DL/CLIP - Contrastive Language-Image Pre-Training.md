Created: 2022-07-01 10:02
#paper

## Main idea
CLIP is a multimodal model released by OpenAI. It works very well in Zero-shot learning tasks.
A CLIP model consists of two encoders, one for texts and the other for images, that map images and texts to the same mathematical space. CLIP is then trained to predict how likely the image corresponds to the text using contrastive pre-training.
![[CLIP_encoders.png]]

## References
1. [Paper](https://arxiv.org/pdf/2103.00020.pdf)
2. [OpenAI Blog](https://openai.com/blog/clip/)
3. [Papers with Code](https://paperswithcode.com/method/clip)
4. [Higging Face](https://huggingface.co/docs/transformers/model_doc/clip)
5. [Analyrics India](https://analyticsindiamag.com/how-clip-is-changing-computer-vision-as-we-know-it/)
6. [KDNuggets](https://www.kdnuggets.com/2021/03/beginners-guide-clip-model.html)

## Code
1. [GitHub](https://github.com/openai/CLIP)
2. [Example for classification](https://colab.research.google.com/drive/1LXla2q9MCRRI_kTjpvag2Vz-7EGLnki5#scrollTo=lOF3Feb7jrnu)
3. [Towards Data Science](https://towardsdatascience.com/linking-images-and-text-with-openai-clip-abb4bdf5dbd2)
4. [How to implement CLIP](https://towardsdatascience.com/simple-implementation-of-openai-clip-model-a-tutorial-ace6ff01d9f2)
