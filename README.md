# [Dataset] IndicEval-XL : Bridging Linguistic Diversity in Code Generation Across Indic Languages
 
This repository contains the IndicEval-XL, a comprehensive benchmark for code generation that incorporates 5 major Indic languages, collectively spoken by approximately 14% of the world's population. so as to make AI-powered
development tools more inclusive and accessible to developers
of various linguistic backgrounds. Results and findings can be found in the paper "IndicEval-XL : Bridging Linguistic Diversity in Code Generation Across Indic Languages" (link).
We as Deutsche Telekom, hence this entire dataset is availble under MIT license, so its free to use and redistribute for research purposes.

## Paper summary
The paper highlights both the potential and challenges of multilingual code generation, emphasizing the need for more inclusive AI systems that can serve developers across diverse linguistic backgrounds. It provides valuable insights for future research directions in enhancing models for low-resource languages and developing more nuanced evaluation metrics. We have adopted the following framework for this.
 
![Alt text] (image path)
### Evaluation Methodology
 
We employed robust evaluation methodologies:
 
1. **CodeBERTScore**: Our primary metric that leverages contextual embeddings to assess semantic similarity, ensuring generated code maintains functional correctness across different languages.
 
2. **BERTScore**: Our secondary metric that leverages the pre-trained contextual embeddings from BERT and matches words in candidate and reference sentences by cosine similarity.
 
3. **Pass@k**: Though we recognize limitations with this metric (particularly for smaller LLMs that may produce functionally correct code with minor naming discrepancies), we include pass@k scores and test cases for traditional evaluation.
 
### Key Findings
 
1. **Model Performance**: Across evaluated models (Gemini 1.5, Gemini 2.0, and LLaMA 7B), Gemini models(LLMs) demonstrated superior performance compared to LLaMA 7B (SLMs).
 
2. **Language-Specific Performance**:
   - High alignment: JavaScript, Python, and PHP recorded the highest CodeBERTScores
   - Moderate alignment: Java and Scala showed comparatively lower scores
   - Among Indic languages: Hindi, Urdu, and Punjabi achieved highest alignment scores
   - Sanskrit emerged as the most challenging Indic language (likely due to limited training data)
 
## Dataset Details
 
IndicEval-XL contains two primary datasets:
 
1. **HumanEval-XXL**: A multilingual code generation dataset comprising 29 NL-PL pairs of problems:
   - 22 from HumanEval-XL
   - 7 from IndicEval-XL
 
2. **IndicEval-XL**: Primarily focuses on 6 Indic Languages and includes:
   - 6,720 coding problems
   - 12 Programming Languages (same as in HumanEval-XL)
   - 7 Natural Languages (English + 6 Indic languages)
 
**Languages**
- The 7 natural languages included in our dataset:
Hindi, Sanskrit, Punjabi, Urdu, Tamil, Marathi and English 
- The 12 programming languages included:
Python, Java, Go, Kotlin, PHP, Ruby, Scala, JavaScript, C#, Perl, Swift, and TypeScript.
 
## Usage
 
The dataset is free to use and accessible for benchmarking LLMs along with other datasets and benchmarks. All content used in this dataset is free to use and redistribute in an open and unrestricted manner for research purposes.
 
## Credits 
We adapted Microsoft's codebert package (https://github.com/microsoft/CodeBERT) and BertScore (https://github.com/Tiiiger/bert_score) for the evaluation We thank them for their pioneering effort in this field including the release of the dataset and evaluation code. We thank OpenAI for their pioneering effort in this field including the release of the original HumanEval dataset which we convert to the multi-lingual versions and Amazon-Science's mxeval (https://github.com/amazon-science/mxeval?tab=readme-ov-file). We also thank HumanEval-XL for their release of the dataset (https://github.com/FloatAI/humaneval-xl), which we have adapted for Indic languages.
 
 
## Citation
 
Please cite using the following bibtex entry:
```
@article{singh2025indiceval,
  title={IndicEval-XL: Bridging Linguistic Diversity in Code Generation Across Indic Languages},
  author={Singh, Ujjwal and Sharma, Aditi and Gupta, Nikhil and Deepakshi and Jha, Vivek Kumar},
  year={2025},
  publisher={Deutsche Telekom Digital Labs}
}
```
