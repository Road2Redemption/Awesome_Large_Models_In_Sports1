<div align="center">
  <h1><img src="assets/title.png" alt="" width="56" align="absmiddle"> Awesome Large Models in Sports</h1>
  <p><strong>A living survey and curated research hub for large language and multimodal models in sports</strong></p>
  
  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  [![Paper](https://img.shields.io/badge/ACL%202026-Findings-1f6f8b.svg)](https://aclanthology.org/2026.findings-acl.1851/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
  ![](https://img.shields.io/github/last-commit/Road2Redemption/Awesome_Large_Models_In_Sports1?color=green) 

  <p>
    <em>Yichen Xu, Jianzhe Ma, Chuhan Wang, Zhonghao Cao, Liangyu Chen, Wenxuan Wang, and Qin Jin</em><br>
    Findings of the Association for Computational Linguistics: ACL 2026
  </p>

</div>


---

## 🔔 News

- **[2026-08-01]** 🔎 We expanded the living bibliography with papers first released from **July 2025 through July 2026**, including new work from arXiv, alphaXiv, and SportRxiv.
- **[2026-04-04]** 🎉 Our survey was accepted to **Findings of ACL 2026**.
- **[2025-10-21]** 📄 We released the preprint of ["A Survey of Large Models in Sports"](https://www.researchgate.net/publication/396734233_A_Survey_of_Large_Models_in_Sports).
- **[2025-10-13]** 🚀 We launched this repository as a living collection of research on large models in sports.

---

## Paper

> **Accepted to Findings of ACL 2026 on April 4, 2026.**<br>
> Yichen Xu, Jianzhe Ma, Chuhan Wang, Zhonghao Cao, Liangyu Chen, Wenxuan Wang, and Qin Jin.<br>
> *A Survey of Large Models in Sports.* Findings of ACL 2026, pages 37154–37189.

| Read | Cite | Explore |
| --- | --- | --- |
| [ACL Anthology](https://aclanthology.org/2026.findings-acl.1851/) · [PDF](https://aclanthology.org/2026.findings-acl.1851.pdf) | [BibTeX](paper.bib) · [Citation metadata](CITATION.cff) | [Interactive literature index](https://road2redemption.github.io/Awesome_Large_Models_In_Sports1/) · [Topic list](#-table-of-contents) |

### The survey in two figures

| Application landscape | Research taxonomy |
| --- | --- |
| [<img src="applications.jpg" alt="Applications of large models across six sports stakeholder groups" width="100%">](applications.jpg) | [<img src="taxonomy.png" alt="Taxonomy of large models in sports" width="100%">](taxonomy.png) |
| Six stakeholder groups connect large models to real participants in sport. | Topics, tasks, and datasets form the structure used throughout this repository. |

---

## About This Collection

This repository is the living bibliography for our survey. It covers research that uses large language models or multimodal large models to understand, analyze, generate, or support activities in sport. Papers are organized by the participant-centered taxonomy introduced in the survey rather than by model family.

### Scope of the survey

- **A participant-centered taxonomy** covering athletes and trainers, coaches and educators, referees, fans and media, researchers, and the sports industry.
- **A structured map of tasks and applications**, from personalized coaching and injury rehabilitation to tactics, refereeing, commentary, highlights, and talent scouting.
- **A review of sports datasets and benchmarks** for language, vision, video, audio, sensor, and multimodal research.
- **A critical research agenda** highlighting open challenges and future directions for reliable, responsible, and practically useful sports intelligence.

> New to the field? Start with the [paper](https://aclanthology.org/2026.findings-acl.1851/) for the full taxonomy and analysis, then use the [table of contents](#-table-of-contents) below to explore papers by application area.

### At a glance

| Survey scope | Repository coverage |
| --- | --- |
| **6 stakeholder groups** | Athletes, coaches, referees, fans, researchers, and industry |
| **28 research topics** | From training prescription to multimodal sports understanding |
| **263 unique works** | Searchable in the [interactive research catalog](https://road2redemption.github.io/Awesome_Large_Models_In_Sports1/) |
| **2020–2026 literature** | Updated through **July 31, 2026** and organized by the taxonomy introduced in our ACL 2026 paper |

For literature updates, we use the paper's **first public release date** to determine whether it falls inside the update window; later revisions of earlier preprints are not counted as newly released papers. We include work in which an LLM, MLLM, VLM, or closely related large-model system is central to the sports task, dataset, benchmark, or analysis. See the [literature search protocol](LITERATURE_SEARCH.md) for the sources and screening rules.

We organize the applications into **six major stakeholder groups** ([see the application landscape](applications.jpg)):

1. **Athletes & Trainers** – exercise and training plans, injury prevention, rehabilitation, and sports psychology  
2. **Coaches & Educators** – action recognition, performance prediction, and tactics or strategies  
3. **Referees** – decision support, fairness, and explainable refereeing systems  
4. **Fans & Media** – commentary, highlights, storytelling, news, sentiment analysis and general sports models
5. **Researchers** – academic writing and knowledge discovery in sports science  
6. **The Sports Industry** – management, talent scouting, and tourism applications  


We further structure the repository following the **[taxonomy tree](taxonomy.png)** introduced in our paper, offering a clear overview of research topics, tasks, and datasets within each stakeholder group.

This collection serves as an open, evolving resource for researchers, developers, and sports enthusiasts passionate about exploring how frontier AI is transforming sports — and discovering what Large Models can bring to the next generation of **sports intelligence**.

## ⭐ Featured Reading Paths

Use these paths to move from the survey to representative research areas:

| If you are interested in... | Start with... |
| --- | --- |
| Athlete-facing AI | [Training prescription](#training-prescription-and-plans), [injury and rehabilitation](#sports-injury-and-rehabilitation), and [sports psychology](#sports-psychology-and-behavior) |
| Sports video intelligence | [Action spotting](#action-spotting-and-recognition), [action quality assessment](#sports-action-quality-assessment), and [sports understanding](#sports-understanding) |
| Coaching and competition | [Tactics and strategies](#sports-tactics-and-strategies) and [performance prediction](#game-and-player-performance-prediction) |
| Media and fan experiences | [Commentary](#sports-commentary-generation), [highlights](#sports-highlight-generation), and [storytelling](#sports-narratives-and-storytelling) |
| Responsible deployment | [Refereeing](#sports-refereeing), [public opinion](#public-opinion-analysis-in-sports), and the challenges discussed in the [survey](https://aclanthology.org/2026.findings-acl.1851/) |

---

## 📜 Table of Contents

- [Featured Reading Paths](#-featured-reading-paths)
- [Applications for Athletes and Trainers](#applications-for-athletes-and-trainers)
  - [Training Prescription and Plans](#training-prescription-and-plans)
  - [Sports Injury and Rehabilitation](#sports-injury-and-rehabilitation)
  - [Sports Psychology and Behavior](#sports-psychology-and-behavior)
- [Applications for Coaches and Educators](#applications-for-coaches-and-educators)
  - [Action Spotting and Recognition](#action-spotting-and-recognition)
  - [Sports Action Quality Assessment](#sports-action-quality-assessment)
  - [Sports Tactics and Strategies](#sports-tactics-and-strategies)
  - [Game and Player Performance Prediction](#game-and-player-performance-prediction)
  - [Sports Education](#sports-education)
- [Applications for Referees](#applications-for-referees)
  - [Sports Refereeing](#sports-refereeing)
- [Applications for Fans and Media](#applications-for-fans-and-media)
  - [Sports Commentary Generation](#sports-commentary-generation)
  - [Sports Highlight Generation](#sports-highlight-generation)
  - [Sports News Generation](#sports-news-generation)
  - [Sports Narratives and Storytelling](#sports-narratives-and-storytelling)
  - [Public Opinion Analysis in Sports](#public-opinion-analysis-in-sports)
  - [Sports Models and Systems](#sports-models-and-systems)
- [Applications for Researchers](#applications-for-researchers)
  - [Sports Academic Writing](#sports-academic-writing)
- [Applications for the Sports Industry](#applications-for-the-sports-industry)
  - [Sports Management](#sports-management)
  - [Sports Talent Scouting](#sports-talent-scouting)
  - [Sports Tourism](#sports-tourism)
- [Sports Understanding](#sports-understanding)
  - [Specialized Sports Understanding](#specialized-sports-understanding)
  - [General Video Understanding](#general-video-understanding)
- [Related Surveys](#related-surveys)
- [Year Index](#year-index)
  - [2020](#2020)
  - [2021](#2021)
  - [2022](#2022)
  - [2023](#2023)
  - [2024](#2024)
  - [2025](#2025)


## Applications for Athletes and Trainers

### Training Prescription and Plans

1. **Artificial Intelligence in Sport: Exploring the Potential of Using ChatGPT in Resistance Training Prescription**, Biology of sport 2024 [[paper](https://www.termedia.pl/Artificial-intelligence-in-sport-Exploring-the-potential-of-using-r-nChatGPT-in-resistance-training-prescription,78,51817,0,1.html )]
2. **Using Artificial Intelligence for Exercise Prescription in Personalised Health Promotion: a Critical Evaluation of OpenAI’s GPT-4 Model**, Biology of Sport 2024 [[paper](https://www.termedia.pl/Using-artificial-intelligence-for-exercise-prescription-in-personalised-health-promotion-A-critical-evaluation-of-OpenAI-s-GPT-4-model,78,52030,1,1.html)]
3. **ChatGPT and Exercise Prescription: Human vs. Machine or Human Plus Machine?**, Journal of Sport and Health Science 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S2095254623001060)]
4. **Infusing Behavior Science into Large Language Models for Activity Coaching**, PLOS Digital Health 2024 [[paper](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000431)]
5. **The Potential of Large Language Model Chatbots for Application to Epilepsy: Let’s Talk About Physical Exercise**, Epilepsy & Behavior Reports 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S2589986424000492)]
6. **Towards a Personal Health Large Language Model**, AIM-FM Workshop @ NeurIPS'24 Oral 2024 [[paper](https://openreview.net/forum?id=1Fbna6cNPw)]
7. **Visualizing Exercise Data from Combat Exergame for Exploring the Insight from Personal Informatics with Large Language Models**, CHI EA 2025 [[paper](https://dl.acm.org/doi/abs/10.1145/3706599.3720165)]
8. **Reproducibility and Quality of Hypertrophy-Related Training Plans Generated by GPT-4 and Google Gemini as Evaluated by Coaching Experts**, Biology of Sport 2025 [[paper]( https://pubmed.ncbi.nlm.nih.gov/40182716/)]
9. **Evaluating the Potential Role of AI Chatbots in Designing Personalized Exercise Programs for Weight Management**, International Journal of Human–Computer Interaction 2025 [[paper](https://www.tandfonline.com/doi/full/10.1080/10447318.2025.2462752)]
10. **Acceptance and Trust in AI-Generated Exercise Plans Among Recreational Athletes and Quality Evaluation by Experienced Coaches a Pilot Study**, BMC Research Notes 2025 [[paper](https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-025-07172-9)]
11. **Can People with Epilepsy Trust AI Chatbots for Information on Physical Exercise?**,  Epilepsy & Behavior 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S1525505024005754)]
12. **GPTCoach: Towards LLM-Based Physical Activity Coaching**, CHI 2025 [[paper](https://dl.acm.org/doi/abs/10.1145/3706598.3713819)]
13. **Digital Coaches: an Alternative to Expert Coaches for Men's Fitness Goals**, Physical Activity Review 2025 [[paper](https://www.researchgate.net/publication/392219663_Digital_coaches_an_alternative_to_expert_coaches_for_men's_fitness_goals)]
14. **A Multi-Agent Digital Twin Framework for AI-Driven Fitness Coaching**, IMX 2025 [[paper](https://dl.acm.org/doi/10.1145/3706370.3731651)]
15. **GPT‑ 4 as a Virtual Fitness Coach: a Case Study Assessing Its Effectiveness in Providing Weight Loss and Fitness Guidance**, BMC Public Health 2025 [[paper](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-22739-8)]
16. **T3Set: a Multimodal Dataset with Targeted Suggestions for LLM-Based Virtual Coach in Table Tennis Training**, KDD 2025 [[paper](https://dl.acm.org/doi/10.1145/3711896.3737407)]
17. **Table Tennis Coaching System Based on a Multimodal Large Language Model with a Table Tennis Knowledge Base**, PloS one 2025 [[paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0317839)]
18. **Enhancing Athletic Performance Through AI: an Iterative Prompt Engineering Approach for LLM-Based Coaching Feedback**, International Conference on Human-Computer Interaction 2025 [[paper](https://link.springer.com/chapter/10.1007/978-3-031-94171-9_22)]
19. **Intent-Aware Personalized Feedback Generation from Coach-Athlete Dialogues in Sports Training**, Journal of King Saud University Computer and Information Sciences 2025 [[paper](https://link.springer.com/article/10.1007/s44443-025-00165-5)]
20. **Balancing Act: Generative AI Tools and Scope of Practice in Health Coaching**, American Journal of Health Promotion 2025 [[paper](https://journals.sagepub.com/doi/abs/10.1177/08901171251340383)]
21. **Examining the Ability of Artificial Intelligence with ChatGPT-4.0 to Create an Exercise Program: Case Scenario Examples "Lumbar Disc Herniation, Chronic Migraine, and Urge Urinary Incontinence**, Turkish Journal of Kinesiology 2025[[paper](https://dergipark.org.tr/en/pub/turkjkin/issue/90094/1617953)]
22. **ChatGPT-4o-Generated Exercise Plans for Patients with Type 2 Diabetes Mellitus—Assessment of Their Safety and Other Quality Criteria by Coaching Experts**, IEEE Access 2025 [[paper](https://www.mdpi.com/2075-4663/13/4/92)]
23. **Harnessing Generative Artificial Intelligence for Exercise and Training Prescription: Applications and Implications in Sports and Physical Activity—A Systematic Literature Review**, Applied Sciences 2025 [[paper](https://www.mdpi.com/2076-3417/15/7/3497)]
24. **Optimizing Athletic Performance Through Advanced Nutrition Strategies: Can AI and Digital Platforms Have a Role in Ultraendurance Sports?**, Biology of Sport 2024 [[paper](https://www.termedia.pl/Optimizing-athletic-performance-through-advanced-nutrition-r-nstrategies-can-AI-and-digital-platforms-have-a-role-in-ultraendurance-sports-,78,54384,0,1.html)]
25. **The Sports Nutrition Knowledge of Large Language Model (LLM) Artificial Intelligence (AI) Chatbots: an Assessment of Accuracy, Completeness, Clarity, Quality of Evidence, and Test-Retest Reliability**, PLOS One 2025 [[paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0325982)]
26. **ExpertAF: Expert Actionable Feedback from Video**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ashutosh_ExpertAF_Expert_Actionable_Feedback_from_Video_CVPR_2025_paper.html)]
27. **LEGOLAS: Learning & Enhancing Golf Skills Through LLM-Augmented System**, CHI EA 2025 [[paper](https://dl.acm.org/doi/10.1145/3706599.3720141)]
28. **Expert Comment Generation Considering Sports Skill Level Using a Large Multimodal Model with Video and Spatial-Temporal Motion Features**, Sensors 2025 [[paper](https://www.mdpi.com/1424-8220/25/2/447)]
29. **MAAIG: Motion Analysis and Instruction Generation**, MM Asia 2023 [[paper](https://arxiv.org/abs/2311.00980)]
30. **MotionGPT-2: a General-Purpose Motion-Language Model for Motion Generation and Understanding**, arXiv:2410.21747 [[paper](https://arxiv.org/abs/2410.21747)]
31. **CoachMe: Decoding Sport Elements with a Reference-Based Coaching Instruction Generation Model**, ACL 2025 [[paper](https://aclanthology.org/2025.acl-long.1413/)]
32. **Who Could and Should Give Exercise Prescription: Physicians, Exercise and Health Scientists, Fitness Trainers, or ChatGPT?**, Journal of Sport and Health Science 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S2095254624000012)]
33. **Does ChatGPT Provide Comprehensive and Accurate Information Regarding the Effects, Types and Programming of Core Exercises?**, Turkish Journal of Kinesiology 2024 [[paper](https://dergipark.org.tr/en/pub/turkjkin/article/1516614)]
34. **ChatGPT Generated Training Plans for Runners Are Not Rated Optimal by Coaching Experts, but Increase in Quality with Additional Input Information**, Journal of sports science & medicine 2024 [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10915606/)]
35. **The Impact of LLM Hallucinations on Motor Skill Learning: a Case Study in Badminton**, IEEE Access 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10638024)]
36. **RAG-LLM Based Evaluation Pathway and Technological Exploration for the Scientific Validity of Mass Fitness**, ASSC 6th 2025 [[paper](https://www.researchgate.net/profile/Kyungsik-Kim-6/publication/393279373_E-proceeding_of_2025_6th_Asia_Sport_Science_Conference/links/6864f099b991270ef300f0cc/E-proceeding-of-2025-6th-Asia-Sport-Science-Conference.pdf#page=272)]
37. **Characteristics and Perceived Suitability of Artificial Intelligence-Driven Sports Coaches: a Pilot Study on Psychological and Perceptual Factors**, Frontiers in Sports and Active Living 2025 [[paper](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1548980/full)]
38. **Assessment of Personalized Exercise Prescriptions Issued by ChatGPT 4.0 and Intelligent Health Promotion Systems for Patients with Hypertension Comorbidities Based on the Transtheoretical Model: A Comparative Analysis**, Journal of Multidisciplinary Healthcare 2024 [[paper](https://www.tandfonline.com/doi/full/10.2147/JMDH.S477452)]
39. **A 10-Week Large Language Model (LLM)-Generated Versus Human-Made Volleyball Training Program on the Jumping Performance of Collegiate Volleyball Athletes**, Journal of Physical Education 2025 [[paper](https://www.scielo.br/j/jpe/a/TQjv6PxVVQcx47xd4FQfqzx/?lang=en)]
40. **The AI Coach: A 5-Week AI-Generated Calisthenics Training Program on Health-Related Physical Fitness Components of Untrained Collegiate Students**, Journal of Human Sport and Exercise 2025 [[paper](https://www.jhse.es/index.php/jhse/article/view/ai-generated-calisthenics-training-program)]
41. **The Effects of Chat GPT Generated Exercise Program in Healthy Overweight Young Adults: A Pilot Study**, Journal of Human Sport and Exercise 2025 [[paper](https://www.jhse.es/index.php/jhse/article/view/gpt-chat-generated-exercise-program-healthy-overweight-young-adu)]
42. **Promises and Perils of Generative Artificial Intelligence: A Narrative Review Informing Its Ethical and Practical Applications in Clinical Exercise Physiology**, BMC Sports Science, Medicine and Rehabilitation 2025 [[paper](https://link.springer.com/article/10.1186/s13102-025-01182-7)]
43. **Exploring Large Language Model as an Interactive Sports Coach: Lessons from a Single-Subject Half Marathon Preparation**, arXiv:2509.26593 2025 [[paper](https://arxiv.org/abs/2509.26593)]
44. **SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance**, arXiv:2512.14121 2025 [[paper](https://arxiv.org/abs/2512.14121)]
45. **Generalizing Sports Feedback Generation by Watching Competitions and Reading Books: A Rock Climbing Case Study**, WACV 2026 [[paper](https://arxiv.org/abs/2602.08996)]
46. **Learning Consistent Temporal Grounding between Related Tasks in Sports Coaching**, arXiv:2603.18453 2026 [[paper](https://arxiv.org/abs/2603.18453)]
47. **Digitizing Coaching Intelligence: An Agentic Framework for Holistic Athlete Profiling using VLM and RAG**, arXiv:2606.28570 2026 [[paper](https://arxiv.org/abs/2606.28570)]
48. **Talking Tennis: Language Feedback from 3D Biomechanical Action Recognition**, arXiv:2510.03921 2025 [[paper](https://arxiv.org/abs/2510.03921)]
49. **Synthesizing the Expert: A Validated Multimodal Dataset for Trustworthy AI-Assisted Swimming Coaching**, arXiv:2605.12799 2026 [[paper](https://arxiv.org/abs/2605.12799)]

### Sports Injury and Rehabilitation

1. **The Role of ChatGPT in Sports Trauma: a Mini Review on Strengths and Limits of Open AI Application**, Discover Artificial Intelligence 2023 [[paper](https://link.springer.com/article/10.1007/s44163-023-00093-1)]
2. **Interdisciplinary Inquiry via PanelGPT: Application to Explore Chatbot Application in Sports Rehabilitation**, medRxiv 2023 [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10402232/)]
3. **Artificial Intelligence in Sports Medicine: Could GPT-4 Make Human Doctors Obsolete?**, Annals of Biomedical Engineering 2023 [[paper](https://link.springer.com/article/10.1007/s10439-023-03213-1)]
4. **Artificial Intelligence and ChatGPT in Orthopaedics and Sports Medicine**, Journal of Experimental Orthopaedics 2023 [[paper](https://link.springer.com/article/10.1186/s40634-023-00642-8)]
5. **Chatbot Generative Pre-Trained Transformer and Artificial Intelligence in Sports Physical Therapy and Rehabilitation**, Saudi Journal of Sports Medicine 2023 [[paper](https://journals.lww.com/sjsm/fulltext/2023/23020/chatbot_generative_pre_trained_transformer_and.6.aspx)]
6. **Assessing ChatGPT’s Competency in Addressing Interdisciplinary Inquiries on Chatbot Uses in Sports Rehabilitation: Simulation Study**, JMIR Medical Education 2024 [[paper](https://mededu.jmir.org/2024/1/e51157/)]
7. **Evaluating the Qualitative and Quantitative Performance of Generative AI on Knowledge in Sports Medicine: the Case of GPT**, General Aspects of Applying Generative AI in Higher Education: Opportunities and Challenges 2024 [[paper](https://link.springer.com/chapter/10.1007/978-3-031-65691-0_6)]
8. **Full-Parameter Fine-Tuning Method of LLMs for Sports Injury Prevention and Treatment**, IJMCMC 2025 [[paper](https://www.igi-global.com/article/full-parameter-fine-tuning-method-of-llms-for-sports-injury-prevention-and-treatment/376486)]
9. **Comparative Evaluation of Artificial Intelligence Models GPT-4 and GPT-3.5 in Clinical Decision-Making in Sports Surgery and Physiotherapy: a Cross-Sectional Study**, BMC Medical Informatics and Decision Making 2025 [[paper]( https://link.springer.com/article/10.1186/s12911-025-02996-8)]
10. **Evaluation of the Phi-3-Mini SLM for Identification of Texts Related to Medicine, Health, and Sports Injuries**, ICMI 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11141224)]
11. **Diagnostic Applications of AI in Sports: a Comprehensive Review of Injury Risk Prediction Methods**, Diagnostics 2024 [[paper](https://www.mdpi.com/2075-4418/14/22/2516)]
12. **Standardization of Neuromuscular Reflex Analysis -- Role of Fine-Tuned Vision-Language Model Consortium and OpenAI gpt-oss Reasoning LLM Enabled Decision Support System**, arXiv:2508.12473 2025 [[paper](https://arxiv.org/abs/2508.12473)]
13. **Clinician-Directed Large Language Model Software Generation for Therapeutic Interventions in Physical Rehabilitation**, arXiv:2511.18274 2025 [[paper](https://arxiv.org/abs/2511.18274)]

### Sports Psychology and Behavior

1. **ChatGPT Is a Breakthrough in Science and Education but Fails a Test in Sports and Exercise Psychology**, Baltic Journal of Sport and Health Sciences 2023 [[paper](https://journals.lsu.lt/baltic-journal-of-sport-health/article/view/1341)]
2. **Increasing Physical Activity Using an Just-in-Time Adaptive Digital Assistant Supported by Machine Learning: a Novel Approach for Hyper-Personalised mHealth Interventions**, Journal of Biomedical Informatics 2023 [[paper]( https://www.sciencedirect.com/science/article/pii/S1532046423001569)]
3. **Investigating the Relationship Between Physical Activity and Tailored Behavior Change Messaging: Connecting Contextual Bandit with Large Language Models**, arXiv:2506.07275 [[paper](https://arxiv.org/abs/2506.07275)]
4. **Generative AI in Sport and Exercise Psychology: Exploring Opportunities and Overcoming Challenges**, Sport and Exercise Psychology Review 2025 [[paper](https://researchonline.gcu.ac.uk/en/publications/generative-ai-in-sport-and-exercise-psychology-exploring-opportun)]
5. **Assessment of Recommendations Provided to Athletes Regarding Sleep Education by GPT-4o and Google Gemini: Comparative Evaluation Study**, JMIR Formative Research 2025 [[paper](https://formative.jmir.org/2025/1/e71358)]
6. **Multisport YODA: Leveraging LLMs for Cognition Based Comprehensive Performance Analytics**, MathSport International 2025 [[paper](https://math.uni.lu/midas/events/mathsports2025/files/Booklet.pdf)]
7. **Transforming Wearable Data into Personal Health Insights Using Large Language Model Agents**, arXiv:2406.06464 [[paper](https://arxiv.org/abs/2406.06464)]
8. **Large Language Models for Wearable Sensor-Based Human Activity Recognition, Health Monitoring, and Behavioral Modeling: a Survey of Early Trends, Datasets, and Challenges**, Sensors 2024 [[paper](https://www.mdpi.com/1424-8220/24/15/5045)]
9. **HARGPT: Are LLMs Zero-Shot Human Activity Recognizers?**, FMSys 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10590466)]
10. **LLaSA: Large Multimodal Agent for Human Activity Analysis Through Wearable Sensors**, arXiv 2024 [[paper](https://bashlab.wpi.edu/publications_pdf/imran2024llasa.pdf)]
11. **The Promise of Foundational Large Language Models in Analysis and Interpretation of Wearable Data: Implications for Physical Behavior Research**, SportRxiv 2026 [[paper](https://sportrxiv.org/index.php/server/preprint/view/711)]


## Applications for Coaches and Educators

### Action Spotting and Recognition

1. **Rugby Scene Classification Enhanced by Vision Language Model**, CVPR 2024 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/html/Nonaka_Rugby_Scene_Classification_Enhanced_by_Vision_Language_Model_CVPRW_2024_paper.html)]
2. **ActionAtlas: a VideoQA Benchmark for Domain-Specialized Action Recognition**, NeurIPS 2024 [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f8643596721dbac71d67f89497323efe-Abstract-Datasets_and_Benchmarks_Track.html)]
3. **SV3.3B: a Sports Video Understanding Model for Action Recognition**, arXiv:2507.17844  [[paper](https://arxiv.org/abs/2507.17844)]
4. **Enhancing Sports Strategy with Video Analytics and Data Mining: Assessing the Effectiveness of Multimodal LLMs in Tennis Video Analysis**, arxiv:2507.02904 [[paper](https://arxiv.org/abs/2507.02904)]
5. **Soccer-CLIP: Vision Language Model for Soccer Action Spotting**, IEEE Access 2025 [[paper](https://ieeexplore.ieee.org/document/10916659)]
6. **F³Set: Towards Analyzing Fast, Frequent, and Fine-Grained Events from Videos**, ICLR 2025 [[paper](https://arxiv.org/abs/2504.08222)]
7. **Improving LLM Video Understanding with 16 Frames per Second**, ICML 2025 [[paper](https://openreview.net/forum?id=3H7qAT9Qow)]
8. **Do We Need Large VLMs for Spotting Soccer Actions?**, arXiv:2506.17144 [[paper](https://arxiv.org/pdf/2506.17144)]
9. **Domain Adaptation of VLM for Soccer Video Understanding**, CVPR 2025 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/html/Jiang_Domain_Adaptation_of_VLM_for_Soccer_Video_Understanding_CVPRW_2025_paper.html)]
10. **Breakdance Video Classification in the Age of Generative AI**, arXiv:2510.20287 2025 [[paper](https://arxiv.org/abs/2510.20287)]

### Sports Action Quality Assessment

1. **From Beats to Scores: a Multi-Modal Framework for Comprehensive Figure Skating Assessment**, CVPR 2025 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/html/Wang_From_Beats_to_Scores_A_Multi-Modal_Framework_for_Comprehensive_Figure_CVPRW_2025_paper.html)]
2. **Fine-Tuning Large Multimodal Models for Fitness Action Quality Assessment**, UMAP adjunct 2025 [[paper](https://dl.acm.org/doi/10.1145/3708319.3733684)]
3. **FitnessAgent: a Unified Agent Framework for Open-Set and Personalized Fitness Evaluation**, ICRA 2025 [[paper](https://www.researchgate.net/publication/395222916_FitnessAgent_A_Unified_Agent_Framework_for_Open-Set_and_Personalized_Fitness_Evaluation)]
4. **LLM-FMS: a Fine-Grained Dataset for Functional Movement Screen Action Quality Assessment**, PloS one 2025 [[paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0313707)]
5. **Can Vision Language Models Judge Action Quality? An Empirical Evaluation**, arXiv:2604.08294 2026 [[paper](https://arxiv.org/abs/2604.08294)]
6. **Learning Skill-Attributes for Transferable Assessment in Video**, NeurIPS 2025 [[paper](https://arxiv.org/abs/2511.13993)]

### Sports Tactics and Strategies

1. **TacticalGPT: Uncovering the Potential of LLMs for Predicting Tactical Decisions in Professional Football**, StatsBomb Conference 2023 [[paper](https://blogarchive.statsbomb.com/uploads/2023/10/TacticalGPT-Uncovering-the-Potential-of-LLMs-for-Predicting-Tactical-Decisions-in-Professional-Football.pdf)]
2. **Smartboard: Visual Exploration of Team Tactics with LLM Agent**, IEEE Transactions on Visualization and Computer Graphics 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10670515)]
3. **Using Large Language Models to Generate Baseball Spray Charts in the Absence of Numerical Data, Proceedings of the Institution of Mechanical Engineers**, Part P: Journal of Sports Engineering and Technology 2024 [[paper](https://maloof.princeton.edu/sites/g/files/toruqf1016/files/documents/87Maloof.pdf)]
4. **Can Large Language Models Do Analytical Reasoning?**, arXiv:2403.04031  [[paper](https://arxiv.org/abs/2403.04031)]
5. **SportsMetrics: Blending Text and Numerical Data to Understand Information Fusion in LLMs**, ACL 2024 [[paper](https://aclanthology.org/2024.acl-long.17/)]
6. **Large Language Models on Race Commentary: Towards Granular Data in Cycling Analytics**, MLSA 2024 [[paper](https://link.springer.com/chapter/10.1007/978-3-031-86692-0_2)]
7. **When Reasoning Meets Information Aggregation: a Case Study with Sports Narratives**, EMNLP 2024 [[paper](https://aclanthology.org/2024.emnlp-main.246/)]
8. **TacticExpert: Spatial-Temporal Graph Language Model for Basketball Tactics**, arXiv:2503.10722 [[paper](https://arxiv.org/abs/2503.10722)]
9. **ChatMatch: Exploring the Potential of Hybrid Vision–language Deep Learning Approach for the Intelligent Analysis and Inference of Racket Sports**, Computer Speech & Language 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S0885230824000779)]
10. **TacEleven: Generative Tactic Discovery for Football Open Play**, arXiv:2511.13326 2025 [[paper](https://arxiv.org/abs/2511.13326)]

### Game and Player Performance Prediction

1. **Predicting in-Game Actions from Interviews of NBA Players**, Computational Linguistics 2020 [[paper](https://direct.mit.edu/coli/article/46/3/667/93377/Predicting-In-Game-Actions-from-Interviews-of-NBA)]
2. **A Stroke of Genius: Predicting the Next Move in Badminton**, CVPR 2024 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/html/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.html)]
3. **Social Networks and Large Language Models for Division I Basketball Game Winner Prediction**, IEEE Access 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10535112/)]
4. **AI for Handball: Predicting and Explaining the 2024 Olympic Games Tournament with Deep Learning and Large Language Models**, MathSport International 2025 [[paper](https://arxiv.org/abs/2407.15987)]
5. **Analyzing Key Factors Influencing IPL Cricket Scores Using Explainability and Multimodal Data, Journal of Quantitative Analysis in Sports 2025** [[paper](https://www.degruyterbrill.com/document/doi/10.1515/jqas-2025-0006/html)]
6. **Neural Sabermetrics with World Model: Play-by-Play Predictive Modeling with Large Language Model**, arXiv:2602.07030 2026 [[paper](https://arxiv.org/abs/2602.07030)]
7. **KellyBench: A Benchmark for Long-Horizon Sequential Decision Making**, arXiv:2604.27865 2026 [[paper](https://arxiv.org/abs/2604.27865)]
8. **LLM-SoccerArena: Benchmarking LLMs on Real-World Predictions in Sports**, arXiv:2607.24573 2026 [[paper](https://arxiv.org/abs/2607.24573)]

### Sports Education

1. **Proactive Autonomous Assignments as Pedagogical Responses to the Rise of Artificial Intelligence Solutions in Sport Management Teaching Practice**, Sport Management Education Journal 2023 [[paper](https://journals.humankinetics.com/view/journals/smej/19/1/article-p54.xml)]
2. **Artificial Intelligence in Sport Management Education: Playing the AI Game with ChatGPT, Journal of Hospitality**, Leisure, Sport & Tourism Education 2023 [[paper](https://www.sciencedirect.com/science/article/pii/S1473837623000400)]
3. **Artificial Intelligence in Physical Education and Sports: New Horizons with ChatGPT**, Mediterranean Journal of Sport Science 2023 [[paper](https://dergipark.org.tr/en/pub/asbid/issue/80422/1291604)]
4. **Using ChatGPT to Promote College Students’ Participation in Physical Activities and Its Effect on Mental Health**, World Journal of Psychiatry 2024 [[paper]( https://pmc.ncbi.nlm.nih.gov/articles/PMC10921293/)]
5. **Assessing the Practicality of Using Freely Available AI-Based GPT Tools for Coach Learning and Athlete Development**, Frontiers in Sports and Active Living 2025 [[paper](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1627685/full)]
6. **Harnessing Generative AI in Exercise and Sports Science Education Enhancing Real-World Learning and Overcoming Traditional Barriers in Data Analysis**, Advances in Physiology Education, 2025 [[paper](https://pubmed.ncbi.nlm.nih.gov/40080119/)]
7. **Innovating Physical Education with Artificial Intelligence: a Potential Approach**, Frontiers in Psychology 2025 [[paper](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1490966/full)]
8. **Exploring Opportunities and Challenges Toward ChatGPT for Inclusion in Sport Education, Journal of Hospitality**, Leisure, Sport & Tourism Education 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S1473837625000383)]
9. **From Motion Signals to Insights: a Unified Framework for Student Behavior Analysis and Feedback in Physical Education Classes**,  arXiv:2503.06525 [[paper](https://arxiv.org/abs/2503.06525)]
10. **Artificial Intelligence in Physical Education: Comprehensive Review and Future Teacher Training Strategies**, Frontiers in public health 2024 [[paper](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1484848/full)]


## Applications for Referees

### Sports Refereeing

1. **X-VARS: Introducing Explainability in Football Refereeing with Multi-Modal Large Language Models**, CVPR 2024 Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/html/Held_X-VARS_Introducing_Explainability_in_Football_Refereeing_with_Multi-Modal_Large_Language_CVPRW_2024_paper.html)]
2. **Enhancing Football Refereeing with AI: VARS and X-VARS for Assisted Decision-Making**, MathSport International 2025 [[paper](https://orbi.uliege.be/handle/2268/328584)]
3. **RefereeBench: Are Video MLLMs Ready to be Multi-Sport Referees**, arXiv:2604.15736 2026 [[paper](https://arxiv.org/abs/2604.15736)]
4. **SoccerRef-Agents: Multi-Agent System for Automated Soccer Refereeing**, arXiv:2604.23392 2026 [[paper](https://arxiv.org/abs/2604.23392)]
5. **Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding**, arXiv:2607.11844 2026 [[paper](https://arxiv.org/abs/2607.11844)]


## Applications for Fans and Media

### Sports Commentary Generation

1. **Soccer Game Summarization Using Audio Commentary, Metadata, and Captions**, NarSUM 2022 [[paper](https://dl.acm.org/doi/abs/10.1145/3552463.3557019)]
2. **Soccer Artificial Intelligence Commentary Service on the Base of Video Analytic and Large Language Models**, TELFOR 2023 [[paper]( https://ieeexplore.ieee.org/abstract/document/10372671)]
3. **MatchTime: Towards Automatic Soccer Game Commentary Generation**, EMNLP 2024 [[paper](https://aclanthology.org/2024.emnlp-main.99/)]
4. **Commentary Generation from Data Records of Multiplayer Strategy Esports Game**, NAACL 2024 Student Research Workshop [[paper](https://aclanthology.org/2024.naacl-srw.28/)]
5. **Personalized Video Comment Generation**, EMNLP Findings 2024 [[paper]( https://aclanthology.org/2024.findings-emnlp.979.pdf)]
6. **AiCommentator: a Multimodal Conversational Agent for Embedded Visualization in Football Viewing**, IUI 2024 [[paper]( https://dl.acm.org/doi/abs/10.1145/3640543.3645197)]
7. **SCBench: a Sports Commentary Benchmark for Video LLMs**,  arXiv:2412.17637 [[paper](https://arxiv.org/abs/2412.17637)]
8. **Designing for Automated Sports Commentary Systems**, IMX 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3639701.3656323)]
9. **LLM-Commentator: Novel Fine-Tuning Strategies of Large Language Models for Automatic Commentary Generation Using Football Event Data**, Knowledge-Based Systems 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S0950705124008530)]
10. **Large Scale Generative AI Text Applied to Sports and Music**,ACM SIGKDD 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3637528.3671542)]
11. **A Descriptive Basketball Highlight Dataset for Automatic Commentary Generation**, MM 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3664647.3681178)]
12. **TimeSoccer: an End-to-End Multimodal Large Language Model for Soccer Commentary Generation**, arXiv:2504.17365 [[paper](https://arxiv.org/abs/2504.17365)]
13. **Domain Adaptation of VLM for Soccer Video Understanding**, CVPR 2025 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/html/Jiang_Domain_Adaptation_of_VLM_for_Soccer_Video_Understanding_CVPRW_2025_paper.html)]
14. **Live Football Commentary System Providing Background Information**, ACL demo 2025 [[paper]( https://aclanthology.org/2025.acl-demo.38/)]
15. **Player Tracking-Integrated Soccer Game Commentary Generation**, IJSAT 2025 [[paper](https://www.ijsat.org/research-paper.php?id=3312)]
16. **LiveCC: Learning Video LLM with Streaming Speech Transcription at Scale**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_LiveCC_Learning_Video_LLM_with_Streaming_Speech_Transcription_at_Scale_CVPR_2025_paper.html)]
17. **Multi-Modal Large Language Model with RAG Strategies in Soccer Commentary Generation**, WACV 2025 [[paper]( https://ieeexplore.ieee.org/abstract/document/10943875)]
18. **Player-Centric Multimodal Prompt Generation for Large Language Model Based Identity-Aware Basketball Video Captioning**, ICCV 2025 [[paper](https://arxiv.org/abs/2507.20163)]
19. **Enhanced Cricket Commentary Using AI Vision and Multilingual Translation**, IEEE International Conference on Emerging Technologies and Applications (MPSec ICETA), IEEE 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11118722)]
20. **Temporally-Grounded Language Generation: a Benchmark for Real-Time Vision-Language Models**, arXiv:2505.11326 [[paper](https://arxiv.org/abs/2505.11326)]
21. **StreamMind: Unlocking Full Frame Rate Streaming Video Dialogue Through Event-Gated Cognition**, arXiv:2503.06220 [[paper](https://arxiv.org/abs/2503.06220)]
22. **Commentary Generation for Soccer Highlights**, arXiv:2508.07543 2025 [[paper](https://arxiv.org/abs/2508.07543)]
23. **Large VLM-based Stylized Sports Captioning**, arXiv:2508.19295 2025 [[paper](https://arxiv.org/abs/2508.19295)]
24. **TennisExpert: Towards Expert-Level Analytical Sports Video Understanding**, arXiv:2603.13397 2026 [[paper](https://arxiv.org/abs/2603.13397)]
25. **MCAD: Multimodal Context-Aware Audio Description Generation for Soccer**, arXiv:2511.09448 2025 [[paper](https://arxiv.org/abs/2511.09448)]
26. **Real-Time Generation of Game Video Commentary with Multimodal LLMs: Pause-Aware Decoding Approaches**, LREC 2026 [[paper](https://arxiv.org/abs/2603.02655)]
27. **BoxComm: Benchmarking Category-Aware Commentary Generation and Narration Rhythm in Boxing**, arXiv:2604.04419 2026 [[paper](https://arxiv.org/abs/2604.04419)]


### Sports Highlight Generation

1. **Multi-Modal Architecture for Cricket Highlights Generation: Using Computer Vision and Large Language Model**, ICOSST 2023 [[paper](https://ieeexplore.ieee.org/abstract/document/10414235/)]
2. **AI-Based Sports Highlight Generation for Social Media**, MHV 2024 [[paper]( https://dl.acm.org/doi/abs/10.1145/3638036.3640799)]
3. **Survey Paper on AI Based Sports Highlight Generation for Social Media**, Journal of Scientific Research and Technology 2025 [[paper]( https://www.jsrtjournal.com/index.php/JSRT/article/view/194)]
4. **DIAMOND: an LLM-Driven Agent for Context-Aware Baseball Highlight Summarization**, REALM 2025 [[paper]( https://aclanthology.org/2025.realm-1.28/)]
5. **HIPPO-VIDEO: Simulating Watch Histories with Large Language Models for History-Driven Video Highlighting**, COLM 2025 [[paper](https://www.arxiv.org/abs/2507.16873)]
6. **SportSummarizer: a Unified Multimodal Fusion Transformer for Context-Aware Sports Video Summarization**, Neurocomputing 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S0925231225016832)]
7. **SVHighlights: Towards Extremely Long Sport Video Highlight Detection**, KDD 2026 [[paper](https://arxiv.org/abs/2606.06926)]

### Sports News Generation

1. **SportsSum2.0: Generating High-Quality Sports News from Live Text Commentary**, CIKM 2021 [[paper]( https://dl.acm.org/doi/abs/10.1145/3459637.3482188)]
2. **Knowledge Enhanced Sports Game Summarization**, WSDM 2022 [[paper]( https://dl.acm.org/doi/abs/10.1145/3488560.3498405)]
3. **SNIL: Generating Sports News from Insights with Large Language Models**, IEEE Transactions on Visualization and Computer Graphics 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10507016/)]
4. **Advancing Cricket Narratives: AI-Enhanced Advanced Journaling in the IPL Using Language Models**, CONECCT 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10677234)]
5. **BADGE: BADminton Report Generation and Evaluation with LLM, IJCAI 2024 Workshop**,arXiv:2406.18116 [[paper]( https://arxiv.org/pdf/2406.18116v1)]
6. **Tree-Of-Report: Table-to-Text Generation for Sports Game Reports with Tree-Structured Prompting**, ACL-SRW 2025 [[paper](https://openreview.net/pdf?id=gR4MPb03or)]
7. **Moneyball with LLMs: Analyzing Tabular Summarization in Sports Narratives**, arXiv:2510.18173 2025 [[paper](https://arxiv.org/abs/2510.18173)]
8. **Tree-of-Text: A Tree-Based Prompting Framework for Table-to-Text Generation in the Sports Domain**, arXiv:2604.26501 2026 [[paper](https://arxiv.org/abs/2604.26501)]
9. **SUMMIR: A Hallucination-Aware Framework for Ranking Sports Insights from LLMs**, arXiv:2604.04947 2026 [[paper](https://arxiv.org/abs/2604.04947)]

### Sports Narratives and Storytelling

1. **Generating Factually Consistent Sport Highlights Narrations**, MMSports 2023 [[paper]( https://dl.acm.org/doi/abs/10.1145/3606038.3616157)]
2. **Sportify: Question Answering with Embedded Visualizations and Personified Narratives for Sports Video**, IEEE Transactions on Visualization and Computer Graphics 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10673998)]
3. **Multimodal AI-Based Summarization and Storytelling for Soccer on Social Media**, MMSys 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3625468.3652197)]
4. **Large Scale Generative AI Text Applied to Sports and Music**, ACM SIGKDD 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3637528.3671542)]
5. **SportsBuddy: Designing and Evaluating an AI-Powered Sports Video Storytelling Tool Through Real-World Deployment**, PacificVis 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11021035)]

### Public Opinion Analysis in Sports

1. **Esports Debut as a Medal Event at 2023 Asian Games: Exploring Public Perceptions with BERTopic and GPT-4 Topic Fine-Tuning**, arXiv:2409.18798 [[paper]( https://arxiv.org/abs/2409.18798)]
2. **Experience Is All You Need: a Large Language Model Application of Fine-Tuned GPT-3.5 and RoBERTa for Aspect-Based Sentiment Analysis of College Football Stadium Reviews**, Sport Management Review 2025 [[paper]( https://www.tandfonline.com/doi/full/10.1080/14413523.2024.2386467?src=#abstract)]
3. **OneLove Beyond the Field - a Few-Shot Pipeline for Topic and Sentiment Analysis During the FIFA World Cup in Qatar**, KONVENS 2024 [[paper]( https://aclanthology.org/2024.konvens-main.35/)]
4. **INVESTIGATING THE FACTORS INFLUENCING ADOPTION INTENTIONS OF CHATGPT FOR SPORT EVENTS**, SPORMETRE Beden Eğitimi ve Spor Bilimleri Dergisi 2025 [[paper]( https://dergipark.org.tr/tr/pub/spormetre/issue/92744/1606845)]



### Sports Models and Systems

1. **Megan - a Sports Chatbot Using OpenAI APIs and Django Framework with Python**, International Conference for Convergence in Technology (I2CT) 2024 [[paper]( https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10543499&tag=1)]
2. **BleacherBot: AI Agent as a Sports Co-Viewing Partner**, CHI 2025 [[paper]( https://dl.acm.org/doi/10.1145/3706598.3714178)]
3. **Querying Football Matches for Event Data: Towards Using Large Language Models**, ISACE 2024 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-69073-0_19)]
4. **A System for Triggering Sports Instant Answers on Search Engines, SIGIR 2025** [[paper](https://dl.acm.org/doi/pdf/10.1145/3726302.3731953)]
5. **Demo: Soccer Information Retrieval via Natural Queries Using SoccerRAG**, CBMI 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10859233)]
6. **SoccerRAG: Multimodal Soccer Information Retrieval via Natural Queries**, CBMI 2024 [[paper]( https://ieeexplore.ieee.org/abstract/document/10859209)]
7. **Enhancing Structured-Data Retrieval with GraphRAG: Soccer Data Case Study**, arxiv:2409.17580  [[paper](https://arxiv.org/abs/2409.17580)]
8. **Soccer-GraphRAG: Applications of GraphRAG in Soccer**, IRonGraphs 2024 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-71382-8_1)]
9. **Assessing the Accuracy of Large Language Models in Extracting Latest Cricket Information**, Scientific Journal of Sport and Performance 2025 [[paper]( https://sjsp.aearedo.es/index.php/sjsp/article/view/accuracy-llms-extracting-cricket-data)]
10. **Agentic Generative AI for Media Content Discovery at the National Football League**, 2025 [[paper]( https://www.amazon.science/publications/agentic-generative-ai-for-media-content-discovery-at-the-national-football-league)]
11. **From Play to Replay: Composed Video Retrieval for Temporally Fine-Grained Videos**, arXiv:2506.05274 [[paper](https://arxiv.org/abs/2506.05274)]
12. **Korean Football in-Game Conversation State Tracking Dataset for Dialogue and Turn Level Evaluation**, Engineering Applications of Artificial Intelligence 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S0952197624017305)]
13. **FootGPT : a Large Language Model Development Experiment on a Minimal Setting**, arXiv:2308.08610 [[paper]( https://arxiv.org/abs/2308.08610)]
14. **SoccerChat: Integrating Multimodal Data for Enhanced Soccer Game Understanding**, arXiv:2505.16630 [[paper]( https://arxiv.org/abs/2505.16630)]
15. **Multi-Agent System for Comprehensive Soccer Understanding**, arXiv:2505.03735 [[paper](https://arxiv.org/abs/2505.03735)]
16. **Towards Universal Soccer Video Understanding**, CVPR 2025 [[paper]( https://openaccess.thecvf.com/content/CVPR2025/html/Rao_Towards_Universal_Soccer_Video_Understanding_CVPR_2025_paper.html)]
17. **Domain Adaptation of VLM for Soccer Video Understanding**, CVPR 2025 CVsports Workshop [[paper]( https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/html/Jiang_Domain_Adaptation_of_VLM_for_Soccer_Video_Understanding_CVPRW_2025_paper.html)]
18. **FineQuest: Adaptive Knowledge-Assisted Sports Video Understanding via Agent-of-Thoughts Reasoning**, MM 2025 [[paper]( https://arxiv.org/abs/2509.11796)]
19. **Sporthesia: Augmenting Sports Videos Using Natural Language**, IEEE transactions on visualization and computer graphics 2022 [[paper]( https://ieeexplore.ieee.org/abstract/document/9911988/)]
20. **TennisExpert: Towards Expert-Level Analytical Sports Video Understanding**, arXiv:2603.13397 2026 [[paper](https://arxiv.org/abs/2603.13397)]
21. **SVI-Bench: A Dynamic Microworld for Strategic Video Intelligence**, arXiv:2605.31529 2026 [[paper](https://arxiv.org/abs/2605.31529)]
22. **SPORTSQL: An Interactive System for Real-Time Sports Reasoning and Visualization**, arXiv:2508.17157 2025 [[paper](https://arxiv.org/abs/2508.17157)]


## Applications for Researchers

### Sports Academic Writing

1. **ChatGPT for Sample-Size Calculation in Sports Medicine and Exercise Sciences: a Cautionary Note**, International Journal of Sports Physiology and Performance 2023 [[paper](https://journals.humankinetics.com/view/journals/ijspp/18/10/article-p1219.xml)]
2. **AI Did Not Write This Manuscript, or Did It? Can We Trick the AI Text Detector into Generated Texts? the Potential Future of ChatGPT and AI in Sports & Exercise Medicine Manuscript Generation**, BMJ Open Sport & Exercise Medicine 2023 [[paper](https://bmjopensem.bmj.com/content/9/1/e001568)]
3. **From Human Writing to Artificial Intelligence Generated Text: Examining the Prospects and Potential Threats of ChatGPT in Academic Writing**, Biology of sport 2023 [[paper](https://www.termedia.pl/From-human-writing-to-artificial-intelligence-generated-text-examining-the-prospects-and-potential-threats-of-ChatGPT-in-academic-writing,78,50268,0,1.html)]
4. **Artificial Intelligence in Sport Scientific Creation and Writing Process**, Artificial Intelligence in Sports, Movement, and Health 2024 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-67256-9_2)]
5. **Human-Written vs AI-Generated Texts in Orthopedic Academic Literature: Comparative Qualitative Analysis**, JMIR formative research 2024 [[paper]( https://formative.jmir.org/2024/1/e52164)]


## Applications for the Sports Industry

### Sports Management

1. **A Financial Management Maturity Model in Sports Organizations: a Novel Approach Using Artificial Intelligence**, JNSSM 2024 [[paper]( https://jnssm.uk.ac.ir/article_4546_f005ba1018dbf2a9a6984bed3c087ac0.pdf)]
2. **From PDFs to Structured Data: Utilizing LLM Analysis in Sports Database Management**, arXiv:2410.17619 [[paper]( https://arxiv.org/abs/2410.17619)]
3. **Foresight in Sports Businesses: Exploring Emerging Scenarios Based on AI-Language Models and Financial Management Strategies**, Sports Business Journal 2025 [[paper]( https://sbj.alzahra.ac.ir/article_8629.html)]
4. **Comprehensive Site Selection Model for Sports Facilities in Iran: Leveraging AI Language Models**, Sport Management Journal 2025 [[paper]( https://jsm.ut.ac.ir/article_100786_46827a751b01ff496e97ba8034d9c9d3.pdf)]

### Sports Talent Scouting

1. **Empowering the Sports Scientist with Artificial Intelligence in Training, Performance, and Health Management**, Sensors 2024 [[paper]( https://www.mdpi.com/1424-8220/25/1/139)]
2. **Leveraging LLMs and RAG for Enhanced Football Talent Scouting**, CAISE 2025 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-94931-9_24)]
3. **Footyintel: Creating an AI Scout for Better Talent Recognition**, International Journal of Environmental Sciences 2025 [[paper]( https://theaspd.com/index.php/ijes/article/view/1753)]

### Sports Tourism

1. **Investigating Esports Tourism Research Using Artificial Intelligence Applications: ChatGPT Versus ZekAI**, Tourism and Recreation 2025 [[paper](https://dergipark.org.tr/tr/pub/tourismandrecreation/issue/93330/1517704)]
2. **AI-Powered ChatGPT in Sports Tourism Benefits, Challenges, and Future Prospects**, Redefining Tourism With AI and the Metaverse 2025 [[paper](https://www.igi-global.com/chapter/ai-powered-chatgpt-in-sports-tourism/372139)]


## Sports Understanding

### Specialized Sports Understanding

1. **QASports: A Question Answering Dataset about Sports**, Dataset Showcase Workshop (DSW) 2023 [[paper](https://sol.sbc.org.br/index.php/dsw/article/view/25500)]
2. **Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models**, TMLR 2023 [[paper](https://openreview.net/forum?id=uyTL5Bvosj&nesting=2&sort=date-desc)]
3. **Sports-QA: A Large-Scale Video Question Answering Benchmark for Complex and Professional Sports** [[paper](https://arxiv.org/abs/2401.01505)]
4. **SportQA: A Benchmark for Sports Understanding in Large Language Models**, NAACL 2024 [[paper](https://aclanthology.org/2024.naacl-long.283/)]
5. **SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models**, ICLR 2025 [[paper](https://openreview.net/forum?id=x1yOHtFfDh)] 
6. **FSBench: A Figure Skating Benchmark for Advancing Artistic Sports Understanding**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_FSBench_A_Figure_Skating_Benchmark_for_Advancing_Artistic_Sports_Understanding_CVPR_2025_paper.html)] 
7. **LiveCC: Learning Video LLM with Streaming Speech Transcription at Scale**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_LiveCC_Learning_Video_LLM_with_Streaming_Speech_Transcription_at_Scale_CVPR_2025_paper.html)]
8. **Sports Intelligence: Assessing the Sports Understanding Capabilities of Language Models Through Question Answering from Text to Video**, Electronics 2025 [[paper](https://www.mdpi.com/2079-9292/14/3/461)] 
9. **FineBadminton: A Multi-Level Dataset for Fine-Grained Badminton Video Understanding**, MM 2025 [[paper](https://www.arxiv.org/abs/2508.07554)] 
10. **FineQuest: Adaptive Knowledge-Assisted Sports Video Understanding via Agent-of-Thoughts Reasoning**, MM 2025 [[paper](https://arxiv.org/abs/2509.11796)] 
11. **SportR: A Benchmark for Multimodal Large Language Model Reasoning in Sports**, arXiv:2511.06499 2025 [[paper](https://arxiv.org/abs/2511.06499)]
12. **DeepSport: A Multimodal Large Language Model for Comprehensive Sports Video Reasoning via Agentic Reinforcement Learning**, arXiv:2511.12908 2025 [[paper](https://arxiv.org/abs/2511.12908)]
13. **Stepping VLMs onto the Court: Benchmarking Spatial Intelligence in Sports**, arXiv:2603.09896 2026 [[paper](https://arxiv.org/abs/2603.09896)]
14. **TennisExpert: Towards Expert-Level Analytical Sports Video Understanding**, arXiv:2603.13397 2026 [[paper](https://arxiv.org/abs/2603.13397)]
15. **Towards Temporal Compositional Reasoning in Long-Form Sports Videos**, arXiv:2604.22226 2026 [[paper](https://arxiv.org/abs/2604.22226)]
16. **SVI-Bench: A Dynamic Microworld for Strategic Video Intelligence**, arXiv:2605.31529 2026 [[paper](https://arxiv.org/abs/2605.31529)]
17. **Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding**, arXiv:2607.11844 2026 [[paper](https://arxiv.org/abs/2607.11844)]
18. **Let's Play Across Cultures: A Large Multilingual, Multicultural Benchmark for Assessing Language Models' Understanding of Sports**, arXiv:2510.01247 2025 [[paper](https://arxiv.org/abs/2510.01247)]
19. **TennisTV: Do Multimodal Large Language Models Understand Tennis Rallies?**, arXiv:2509.15602 2025 [[paper](https://arxiv.org/abs/2509.15602)]

### General Video Understanding

1.  **InternVid: a Large-Scale Video-Text Dataset for Multimodal Understanding and Generation**, ICLR 2024 [[paper](https://openreview.net/forum?id=MLBdiWu4Fw)]
2.  **E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding**, NeurIPS 2024 [[paper](https://openreview.net/forum?id=KoSSEp6Du5)]
3.  **Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives**, CVPR 2024 [[paper](https://openaccess.thecvf.com/content/CVPR2024/html/Grauman_Ego-Exo4D_Understanding_Skilled_Human_Activity_from_First-_and_Third-Person_Perspectives_CVPR_2024_paper.html)]
4.  **LVBench: an Extreme Long Video Understanding Benchmark**, arXiv:2406.08035 [[paper](https://arxiv.org/abs/2406.08035)]
5.  **VideoVista: a Versatile Benchmark for Video Understanding and Reasoning**,arXiv 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/10982110)]
6.  **FIOVA: a Multi-Annotator Benchmark for Human-Aligned Video Captioning**, arXiv:2410.15270 [[paper](https://arxiv.org/abs/2410.15270)]
7.  **Neptune: the Long Orbit to Benchmarking Long Video Understanding**, arXiv:2412.09582 [[paper](https://arxiv.org/abs/2412.09582)]
8.  **Enhancing Multimodal LLM for Detailed and Accurate Video Captioning Using Multi-Round Preference Optimization**, arXiv:2410.06682 [[paper](https://arxiv.org/abs/2410.06682)]
9.  **Video-SALMONN 2: Captioning-Enhanced Audio-Visual Large Language Models**, arXiv:2506.15220 [[paper](https://arxiv.org/abs/2506.15220)]
10.  **MMWorld: Towards Multi-Discipline Multi-Faceted World Model Evaluation in Videos**, ICLR 2025 [[paper](https://openreview.net/forum?id=tRNKe2Vgqt)]
11.  **LongVILA: Scaling Long-Context Visual Language Models for Long Videos**, ICLR 2025 [[paper](https://openreview.net/forum?id=wCXAlfvCy6)]
12.  **MLVU: Benchmarking Multi-Task Long Video Understanding**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_MLVU_Benchmarking_Multi-task_Long_Video_Understanding_CVPR_2025_paper.html)]
13.  **Video-MME: the First-Ever Comprehensive Evaluation Benchmark of Multi-Modal LLMs in Video Analysis**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Fu_Video-MME_The_First-Ever_Comprehensive_Evaluation_Benchmark_of_Multi-modal_LLMs_in_CVPR_2025_paper.pdf)]
14.  **MotionBench: Benchmarking and Improving Fine-Grained Video Motion Understanding for Vision Language Models**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Hong_MotionBench_Benchmarking_and_Improving_Fine-grained_Video_Motion_Understanding_for_Vision_CVPR_2025_paper.html)]
15.  **OVO-Bench: How Far Is Your Video-LLMs from Real-World Online Video Understanding?**  CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Niu_OVO-Bench_How_Far_is_Your_Video-LLMs_from_Real-World_Online_Video_CVPR_2025_paper.html)]
16.  **VISTA: Enhancing Long-Duration and High-Resolution Video Understanding by VIdeo SpatioTemporal Augmentation**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ren_VISTA_Enhancing_Long-Duration_and_High-Resolution_Video_Understanding_by_Video_Spatiotemporal_CVPR_2025_paper.html)]
17.  **HarmonySet: a Comprehensive Dataset for Understanding Video-Music Semantic Alignment and Temporal Synchronization**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_HarmonySet_A_Comprehensive_Dataset_for_Understanding_Video-Music_Semantic_Alignment_and_CVPR_2025_paper.html)]
18.  **VideoA11y-40K: a Large-Scale Dataset for Accessible Video Understanding** ,  CHI 2025 [[paper](https://dl.acm.org/doi/abs/10.1145/3706598.3714096)]
19.  **TUNA: Comprehensive Fine-Grained Temporal Understanding Evaluation on Dense Dynamic Videos**, ACL 2025 [[paper](https://aclanthology.org/2025.acl-long.91/)]
20.  **WorldSense: Evaluating Real-World Omnimodal Understanding for Multimodal LLMs**, arXiv:2502.04326 [[paper](https://arxiv.org/abs/2502.04326)]
21.  **V-STaR: Benchmarking Video-LLMs on Video Spatio-Temporal Reasoning**, arXiv:2503.11495 [[paper](https://arxiv.org/abs/2503.11495)]
22.  **MINERVA: Evaluating Complex Video Reasoning**, arXiv:2505.00681 [[paper](https://arxiv.org/abs/2505.00681)]
23.  **MAVERIX: Multimodal Audio-Visual Evaluation Reasoning IndeX**, arXiv:2503.21699 [[paper](https://arxiv.org/abs/2503.21699)]
24.  **RTV-Bench: Benchmarking MLLM Continuous Perception, Understanding and Reasoning Through Real-Time Video**, arXiv:2505.02064 [[paper](https://arxiv.org/abs/2505.02064)]
25.  **VidText: Towards Comprehensive Evaluation for Video Text Understanding**, arXiv:2505.22810 [[paper](https://arxiv.org/abs/2505.22810)]
26.  **SIV-Bench: a Video Benchmark for Social Interaction Understanding and Reasoning**, arXiv:2506.05425 [[paper](https://arxiv.org/abs/2506.05425)]
27.  **ExAct: a Video-Language Benchmark for Expert Action Analysis**, arXiv:2506.06277 [[paper](https://arxiv.org/abs/2506.06277)]
28.  **VRBench: a Benchmark for Multi-Step Reasoning in Long Narrative Videos**, arXiv:2506.10857 [[paper](https://arxiv.org/abs/2506.10857)]
29.  **Understanding and Benchmarking the Trustworthiness in Multimodal LLMs for Video Understanding**, arXiv:2506.12336 [[paper](https://arxiv.org/abs/2506.12336)]
30.  **CausalStep: a Benchmark for Explicit Stepwise Causal Reasoning in Videos**, arXiv:2507.16878 [[paper](https://arxiv.org/abs/2507.16878)]
31.  **EgoExoBench: a Benchmark for First- and Third-Person View Video Understanding in MLLMs**, arXiv:2507.18342 [[paper](https://arxiv.org/abs/2507.18342)]
32.  **WildVideo: Benchmarking LMMs for Understanding Video-Language Interaction**, IEEE Transactions on Pattern Analysis and Machine Intelligence 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11097075)]
33.  **ST-VLM: Kinematic Instruction Tuning for Spatio-Temporal Reasoning in Vision-Language Models**, arXiv:2503.19355 [[paper](https://arxiv.org/abs/2503.19355)]
34.  **LiveCC: Learning Video LLM with Streaming Speech Transcription at Scale**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_LiveCC_Learning_Video_LLM_with_Streaming_Speech_Transcription_at_Scale_CVPR_2025_paper.html)]

## Related Surveys

1.  **Artificial intelligence in sport: A narrative review of applications, challenges and future trends**, Journal of Sports Sciences 2025 [[paper](https://www.tandfonline.com/doi/full/10.1080/02640414.2025.2518694)]
2.  **Language and Multimodal Models in Sports: A Survey of Datasets and Applications**, arXiv:2406.12252 [[paper](https://arxiv.org/abs/2406.12252)]
3.  **Large Language Models in Sport Science & Medicine: Opportunities, Risks and Considerations**, arXiv 2023 [[paper](https://arxiv.org/abs/2305.03851)]
4.  **Impact of ChatGPT Technology on Sports Industry**, Journal of New Media and Economics (JNME) 2024 [[paper](http://www.stemmpress.com/jnme/jnme20244/1452.html)]
5.  **Sport and the Promise of Artificial Intelligence: Human and Machine Futures**, Sociology of Sport Journal 2024 [[paper](https://journals.humankinetics.com/view/journals/ssj/aop/article-10.1123-ssj.2024-0150/article-10.1123-ssj.2024-0150.xml)]
6.  **A Review of Artificial Intelligence in Sports: Applications, Ethical Concerns, and Legal Frameworks**, Research Square 2025 [[paper](https://www.researchsquare.com/article/rs-7182432/v1)]
7.  **A deep introspection into the role of ChatGPT for transforming hospitality, leisure, sport, and tourism education**, Journal of Hospitality, Leisure, Sport & Tourism Education 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S1473837624000273)]
8.  **Artificial intelligence in health and sport sciences: Promise, progress, and prudence**, Journal of Sport and Health Science 2025 [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12221458/)]
9.  **Challenges and opportunities of artificial intelligence implementation within sports science and sports medicine teams**, Frontiers in Sports and Active Living 2024 [[paper](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1332427/full)]
10.  **Using Large Language Models to Enhance Exercise Recommendations and Physical Activity in Clinical and Healthy Populations: Scoping Review**, JMIR Medical Informatics 2025 [[paper](https://medinform.jmir.org/2025/1/e59309/)]

## Year Index

> This index is generated from the taxonomy above. Do not edit it manually; run `python3 scripts/generate_year_index.py` after changing paper entries.

<!-- YEAR_INDEX:START -->

### 2026

1. **Generalizing Sports Feedback Generation by Watching Competitions and Reading Books: A Rock Climbing Case Study**, WACV 2026 [[paper](https://arxiv.org/abs/2602.08996)]
1. **Learning Consistent Temporal Grounding between Related Tasks in Sports Coaching**, arXiv:2603.18453 2026 [[paper](https://arxiv.org/abs/2603.18453)]
1. **Digitizing Coaching Intelligence: An Agentic Framework for Holistic Athlete Profiling using VLM and RAG**, arXiv:2606.28570 2026 [[paper](https://arxiv.org/abs/2606.28570)]
1. **Synthesizing the Expert: A Validated Multimodal Dataset for Trustworthy AI-Assisted Swimming Coaching**, arXiv:2605.12799 2026 [[paper](https://arxiv.org/abs/2605.12799)]
1. **The Promise of Foundational Large Language Models in Analysis and Interpretation of Wearable Data: Implications for Physical Behavior Research**, SportRxiv 2026 [[paper](https://sportrxiv.org/index.php/server/preprint/view/711)]
1. **Can Vision Language Models Judge Action Quality? An Empirical Evaluation**, arXiv:2604.08294 2026 [[paper](https://arxiv.org/abs/2604.08294)]
1. **Neural Sabermetrics with World Model: Play-by-Play Predictive Modeling with Large Language Model**, arXiv:2602.07030 2026 [[paper](https://arxiv.org/abs/2602.07030)]
1. **KellyBench: A Benchmark for Long-Horizon Sequential Decision Making**, arXiv:2604.27865 2026 [[paper](https://arxiv.org/abs/2604.27865)]
1. **LLM-SoccerArena: Benchmarking LLMs on Real-World Predictions in Sports**, arXiv:2607.24573 2026 [[paper](https://arxiv.org/abs/2607.24573)]
1. **RefereeBench: Are Video MLLMs Ready to be Multi-Sport Referees**, arXiv:2604.15736 2026 [[paper](https://arxiv.org/abs/2604.15736)]
1. **SoccerRef-Agents: Multi-Agent System for Automated Soccer Refereeing**, arXiv:2604.23392 2026 [[paper](https://arxiv.org/abs/2604.23392)]
1. **Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding**, arXiv:2607.11844 2026 [[paper](https://arxiv.org/abs/2607.11844)]
1. **TennisExpert: Towards Expert-Level Analytical Sports Video Understanding**, arXiv:2603.13397 2026 [[paper](https://arxiv.org/abs/2603.13397)]
1. **Real-Time Generation of Game Video Commentary with Multimodal LLMs: Pause-Aware Decoding Approaches**, LREC 2026 [[paper](https://arxiv.org/abs/2603.02655)]
1. **BoxComm: Benchmarking Category-Aware Commentary Generation and Narration Rhythm in Boxing**, arXiv:2604.04419 2026 [[paper](https://arxiv.org/abs/2604.04419)]
1. **SVHighlights: Towards Extremely Long Sport Video Highlight Detection**, KDD 2026 [[paper](https://arxiv.org/abs/2606.06926)]
1. **Tree-of-Text: A Tree-Based Prompting Framework for Table-to-Text Generation in the Sports Domain**, arXiv:2604.26501 2026 [[paper](https://arxiv.org/abs/2604.26501)]
1. **SUMMIR: A Hallucination-Aware Framework for Ranking Sports Insights from LLMs**, arXiv:2604.04947 2026 [[paper](https://arxiv.org/abs/2604.04947)]
1. **SVI-Bench: A Dynamic Microworld for Strategic Video Intelligence**, arXiv:2605.31529 2026 [[paper](https://arxiv.org/abs/2605.31529)]
1. **Stepping VLMs onto the Court: Benchmarking Spatial Intelligence in Sports**, arXiv:2603.09896 2026 [[paper](https://arxiv.org/abs/2603.09896)]
1. **Towards Temporal Compositional Reasoning in Long-Form Sports Videos**, arXiv:2604.22226 2026 [[paper](https://arxiv.org/abs/2604.22226)]

### 2025

1. **Visualizing Exercise Data from Combat Exergame for Exploring the Insight from Personal Informatics with Large Language Models**, CHI EA 2025 [[paper](https://dl.acm.org/doi/abs/10.1145/3706599.3720165)]
1. **Reproducibility and Quality of Hypertrophy-Related Training Plans Generated by GPT-4 and Google Gemini as Evaluated by Coaching Experts**, Biology of Sport 2025 [[paper]( https://pubmed.ncbi.nlm.nih.gov/40182716/)]
1. **Evaluating the Potential Role of AI Chatbots in Designing Personalized Exercise Programs for Weight Management**, International Journal of Human–Computer Interaction 2025 [[paper](https://www.tandfonline.com/doi/full/10.1080/10447318.2025.2462752)]
1. **Acceptance and Trust in AI-Generated Exercise Plans Among Recreational Athletes and Quality Evaluation by Experienced Coaches a Pilot Study**, BMC Research Notes 2025 [[paper](https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-025-07172-9)]
1. **Can People with Epilepsy Trust AI Chatbots for Information on Physical Exercise?**,  Epilepsy & Behavior 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S1525505024005754)]
1. **GPTCoach: Towards LLM-Based Physical Activity Coaching**, CHI 2025 [[paper](https://dl.acm.org/doi/abs/10.1145/3706598.3713819)]
1. **Digital Coaches: an Alternative to Expert Coaches for Men's Fitness Goals**, Physical Activity Review 2025 [[paper](https://www.researchgate.net/publication/392219663_Digital_coaches_an_alternative_to_expert_coaches_for_men's_fitness_goals)]
1. **A Multi-Agent Digital Twin Framework for AI-Driven Fitness Coaching**, IMX 2025 [[paper](https://dl.acm.org/doi/10.1145/3706370.3731651)]
1. **GPT‑ 4 as a Virtual Fitness Coach: a Case Study Assessing Its Effectiveness in Providing Weight Loss and Fitness Guidance**, BMC Public Health 2025 [[paper](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-22739-8)]
1. **T3Set: a Multimodal Dataset with Targeted Suggestions for LLM-Based Virtual Coach in Table Tennis Training**, KDD 2025 [[paper](https://dl.acm.org/doi/10.1145/3711896.3737407)]
1. **Table Tennis Coaching System Based on a Multimodal Large Language Model with a Table Tennis Knowledge Base**, PloS one 2025 [[paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0317839)]
1. **Enhancing Athletic Performance Through AI: an Iterative Prompt Engineering Approach for LLM-Based Coaching Feedback**, International Conference on Human-Computer Interaction 2025 [[paper](https://link.springer.com/chapter/10.1007/978-3-031-94171-9_22)]
1. **Intent-Aware Personalized Feedback Generation from Coach-Athlete Dialogues in Sports Training**, Journal of King Saud University Computer and Information Sciences 2025 [[paper](https://link.springer.com/article/10.1007/s44443-025-00165-5)]
1. **Balancing Act: Generative AI Tools and Scope of Practice in Health Coaching**, American Journal of Health Promotion 2025 [[paper](https://journals.sagepub.com/doi/abs/10.1177/08901171251340383)]
1. **Examining the Ability of Artificial Intelligence with ChatGPT-4.0 to Create an Exercise Program: Case Scenario Examples "Lumbar Disc Herniation, Chronic Migraine, and Urge Urinary Incontinence**, Turkish Journal of Kinesiology 2025[[paper](https://dergipark.org.tr/en/pub/turkjkin/issue/90094/1617953)]
1. **ChatGPT-4o-Generated Exercise Plans for Patients with Type 2 Diabetes Mellitus—Assessment of Their Safety and Other Quality Criteria by Coaching Experts**, IEEE Access 2025 [[paper](https://www.mdpi.com/2075-4663/13/4/92)]
1. **Harnessing Generative Artificial Intelligence for Exercise and Training Prescription: Applications and Implications in Sports and Physical Activity—A Systematic Literature Review**, Applied Sciences 2025 [[paper](https://www.mdpi.com/2076-3417/15/7/3497)]
1. **The Sports Nutrition Knowledge of Large Language Model (LLM) Artificial Intelligence (AI) Chatbots: an Assessment of Accuracy, Completeness, Clarity, Quality of Evidence, and Test-Retest Reliability**, PLOS One 2025 [[paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0325982)]
1. **ExpertAF: Expert Actionable Feedback from Video**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ashutosh_ExpertAF_Expert_Actionable_Feedback_from_Video_CVPR_2025_paper.html)]
1. **LEGOLAS: Learning & Enhancing Golf Skills Through LLM-Augmented System**, CHI EA 2025 [[paper](https://dl.acm.org/doi/10.1145/3706599.3720141)]
1. **Expert Comment Generation Considering Sports Skill Level Using a Large Multimodal Model with Video and Spatial-Temporal Motion Features**, Sensors 2025 [[paper](https://www.mdpi.com/1424-8220/25/2/447)]
1. **CoachMe: Decoding Sport Elements with a Reference-Based Coaching Instruction Generation Model**, ACL 2025 [[paper](https://aclanthology.org/2025.acl-long.1413/)]
1. **RAG-LLM Based Evaluation Pathway and Technological Exploration for the Scientific Validity of Mass Fitness**, ASSC 6th 2025 [[paper](https://www.researchgate.net/profile/Kyungsik-Kim-6/publication/393279373_E-proceeding_of_2025_6th_Asia_Sport_Science_Conference/links/6864f099b991270ef300f0cc/E-proceeding-of-2025-6th-Asia-Sport-Science-Conference.pdf#page=272)]
1. **Characteristics and Perceived Suitability of Artificial Intelligence-Driven Sports Coaches: a Pilot Study on Psychological and Perceptual Factors**, Frontiers in Sports and Active Living 2025 [[paper](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1548980/full)]
1. **A 10-Week Large Language Model (LLM)-Generated Versus Human-Made Volleyball Training Program on the Jumping Performance of Collegiate Volleyball Athletes**, Journal of Physical Education 2025 [[paper](https://www.scielo.br/j/jpe/a/TQjv6PxVVQcx47xd4FQfqzx/?lang=en)]
1. **The AI Coach: A 5-Week AI-Generated Calisthenics Training Program on Health-Related Physical Fitness Components of Untrained Collegiate Students**, Journal of Human Sport and Exercise 2025 [[paper](https://www.jhse.es/index.php/jhse/article/view/ai-generated-calisthenics-training-program)]
1. **The Effects of Chat GPT Generated Exercise Program in Healthy Overweight Young Adults: A Pilot Study**, Journal of Human Sport and Exercise 2025 [[paper](https://www.jhse.es/index.php/jhse/article/view/gpt-chat-generated-exercise-program-healthy-overweight-young-adu)]
1. **Promises and Perils of Generative Artificial Intelligence: A Narrative Review Informing Its Ethical and Practical Applications in Clinical Exercise Physiology**, BMC Sports Science, Medicine and Rehabilitation 2025 [[paper](https://link.springer.com/article/10.1186/s13102-025-01182-7)]
1. **Exploring Large Language Model as an Interactive Sports Coach: Lessons from a Single-Subject Half Marathon Preparation**, arXiv:2509.26593 2025 [[paper](https://arxiv.org/abs/2509.26593)]
1. **SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance**, arXiv:2512.14121 2025 [[paper](https://arxiv.org/abs/2512.14121)]
1. **Talking Tennis: Language Feedback from 3D Biomechanical Action Recognition**, arXiv:2510.03921 2025 [[paper](https://arxiv.org/abs/2510.03921)]
1. **Full-Parameter Fine-Tuning Method of LLMs for Sports Injury Prevention and Treatment**, IJMCMC 2025 [[paper](https://www.igi-global.com/article/full-parameter-fine-tuning-method-of-llms-for-sports-injury-prevention-and-treatment/376486)]
1. **Comparative Evaluation of Artificial Intelligence Models GPT-4 and GPT-3.5 in Clinical Decision-Making in Sports Surgery and Physiotherapy: a Cross-Sectional Study**, BMC Medical Informatics and Decision Making 2025 [[paper]( https://link.springer.com/article/10.1186/s12911-025-02996-8)]
1. **Evaluation of the Phi-3-Mini SLM for Identification of Texts Related to Medicine, Health, and Sports Injuries**, ICMI 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11141224)]
1. **Standardization of Neuromuscular Reflex Analysis -- Role of Fine-Tuned Vision-Language Model Consortium and OpenAI gpt-oss Reasoning LLM Enabled Decision Support System**, arXiv:2508.12473 2025 [[paper](https://arxiv.org/abs/2508.12473)]
1. **Clinician-Directed Large Language Model Software Generation for Therapeutic Interventions in Physical Rehabilitation**, arXiv:2511.18274 2025 [[paper](https://arxiv.org/abs/2511.18274)]
1. **Investigating the Relationship Between Physical Activity and Tailored Behavior Change Messaging: Connecting Contextual Bandit with Large Language Models**, arXiv:2506.07275 [[paper](https://arxiv.org/abs/2506.07275)]
1. **Generative AI in Sport and Exercise Psychology: Exploring Opportunities and Overcoming Challenges**, Sport and Exercise Psychology Review 2025 [[paper](https://researchonline.gcu.ac.uk/en/publications/generative-ai-in-sport-and-exercise-psychology-exploring-opportun)]
1. **Assessment of Recommendations Provided to Athletes Regarding Sleep Education by GPT-4o and Google Gemini: Comparative Evaluation Study**, JMIR Formative Research 2025 [[paper](https://formative.jmir.org/2025/1/e71358)]
1. **Multisport YODA: Leveraging LLMs for Cognition Based Comprehensive Performance Analytics**, MathSport International 2025 [[paper](https://math.uni.lu/midas/events/mathsports2025/files/Booklet.pdf)]
1. **SV3.3B: a Sports Video Understanding Model for Action Recognition**, arXiv:2507.17844  [[paper](https://arxiv.org/abs/2507.17844)]
1. **Enhancing Sports Strategy with Video Analytics and Data Mining: Assessing the Effectiveness of Multimodal LLMs in Tennis Video Analysis**, arxiv:2507.02904 [[paper](https://arxiv.org/abs/2507.02904)]
1. **Soccer-CLIP: Vision Language Model for Soccer Action Spotting**, IEEE Access 2025 [[paper](https://ieeexplore.ieee.org/document/10916659)]
1. **F³Set: Towards Analyzing Fast, Frequent, and Fine-Grained Events from Videos**, ICLR 2025 [[paper](https://arxiv.org/abs/2504.08222)]
1. **Improving LLM Video Understanding with 16 Frames per Second**, ICML 2025 [[paper](https://openreview.net/forum?id=3H7qAT9Qow)]
1. **Do We Need Large VLMs for Spotting Soccer Actions?**, arXiv:2506.17144 [[paper](https://arxiv.org/pdf/2506.17144)]
1. **Domain Adaptation of VLM for Soccer Video Understanding**, CVPR 2025 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/html/Jiang_Domain_Adaptation_of_VLM_for_Soccer_Video_Understanding_CVPRW_2025_paper.html)]
1. **Breakdance Video Classification in the Age of Generative AI**, arXiv:2510.20287 2025 [[paper](https://arxiv.org/abs/2510.20287)]
1. **From Beats to Scores: a Multi-Modal Framework for Comprehensive Figure Skating Assessment**, CVPR 2025 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/html/Wang_From_Beats_to_Scores_A_Multi-Modal_Framework_for_Comprehensive_Figure_CVPRW_2025_paper.html)]
1. **Fine-Tuning Large Multimodal Models for Fitness Action Quality Assessment**, UMAP adjunct 2025 [[paper](https://dl.acm.org/doi/10.1145/3708319.3733684)]
1. **FitnessAgent: a Unified Agent Framework for Open-Set and Personalized Fitness Evaluation**, ICRA 2025 [[paper](https://www.researchgate.net/publication/395222916_FitnessAgent_A_Unified_Agent_Framework_for_Open-Set_and_Personalized_Fitness_Evaluation)]
1. **LLM-FMS: a Fine-Grained Dataset for Functional Movement Screen Action Quality Assessment**, PloS one 2025 [[paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0313707)]
1. **Learning Skill-Attributes for Transferable Assessment in Video**, NeurIPS 2025 [[paper](https://arxiv.org/abs/2511.13993)]
1. **TacticExpert: Spatial-Temporal Graph Language Model for Basketball Tactics**, arXiv:2503.10722 [[paper](https://arxiv.org/abs/2503.10722)]
1. **ChatMatch: Exploring the Potential of Hybrid Vision–language Deep Learning Approach for the Intelligent Analysis and Inference of Racket Sports**, Computer Speech & Language 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S0885230824000779)]
1. **TacEleven: Generative Tactic Discovery for Football Open Play**, arXiv:2511.13326 2025 [[paper](https://arxiv.org/abs/2511.13326)]
1. **AI for Handball: Predicting and Explaining the 2024 Olympic Games Tournament with Deep Learning and Large Language Models**, MathSport International 2025 [[paper](https://arxiv.org/abs/2407.15987)]
1. **Analyzing Key Factors Influencing IPL Cricket Scores Using Explainability and Multimodal Data, Journal of Quantitative Analysis in Sports 2025** [[paper](https://www.degruyterbrill.com/document/doi/10.1515/jqas-2025-0006/html)]
1. **Assessing the Practicality of Using Freely Available AI-Based GPT Tools for Coach Learning and Athlete Development**, Frontiers in Sports and Active Living 2025 [[paper](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1627685/full)]
1. **Harnessing Generative AI in Exercise and Sports Science Education Enhancing Real-World Learning and Overcoming Traditional Barriers in Data Analysis**, Advances in Physiology Education, 2025 [[paper](https://pubmed.ncbi.nlm.nih.gov/40080119/)]
1. **Innovating Physical Education with Artificial Intelligence: a Potential Approach**, Frontiers in Psychology 2025 [[paper](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1490966/full)]
1. **Exploring Opportunities and Challenges Toward ChatGPT for Inclusion in Sport Education, Journal of Hospitality**, Leisure, Sport & Tourism Education 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S1473837625000383)]
1. **From Motion Signals to Insights: a Unified Framework for Student Behavior Analysis and Feedback in Physical Education Classes**,  arXiv:2503.06525 [[paper](https://arxiv.org/abs/2503.06525)]
1. **Enhancing Football Refereeing with AI: VARS and X-VARS for Assisted Decision-Making**, MathSport International 2025 [[paper](https://orbi.uliege.be/handle/2268/328584)]
1. **TimeSoccer: an End-to-End Multimodal Large Language Model for Soccer Commentary Generation**, arXiv:2504.17365 [[paper](https://arxiv.org/abs/2504.17365)]
1. **Live Football Commentary System Providing Background Information**, ACL demo 2025 [[paper]( https://aclanthology.org/2025.acl-demo.38/)]
1. **Player Tracking-Integrated Soccer Game Commentary Generation**, IJSAT 2025 [[paper](https://www.ijsat.org/research-paper.php?id=3312)]
1. **LiveCC: Learning Video LLM with Streaming Speech Transcription at Scale**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_LiveCC_Learning_Video_LLM_with_Streaming_Speech_Transcription_at_Scale_CVPR_2025_paper.html)]
1. **Multi-Modal Large Language Model with RAG Strategies in Soccer Commentary Generation**, WACV 2025 [[paper]( https://ieeexplore.ieee.org/abstract/document/10943875)]
1. **Player-Centric Multimodal Prompt Generation for Large Language Model Based Identity-Aware Basketball Video Captioning**, ICCV 2025 [[paper](https://arxiv.org/abs/2507.20163)]
1. **Enhanced Cricket Commentary Using AI Vision and Multilingual Translation**, IEEE International Conference on Emerging Technologies and Applications (MPSec ICETA), IEEE 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11118722)]
1. **Temporally-Grounded Language Generation: a Benchmark for Real-Time Vision-Language Models**, arXiv:2505.11326 [[paper](https://arxiv.org/abs/2505.11326)]
1. **StreamMind: Unlocking Full Frame Rate Streaming Video Dialogue Through Event-Gated Cognition**, arXiv:2503.06220 [[paper](https://arxiv.org/abs/2503.06220)]
1. **Commentary Generation for Soccer Highlights**, arXiv:2508.07543 2025 [[paper](https://arxiv.org/abs/2508.07543)]
1. **Large VLM-based Stylized Sports Captioning**, arXiv:2508.19295 2025 [[paper](https://arxiv.org/abs/2508.19295)]
1. **MCAD: Multimodal Context-Aware Audio Description Generation for Soccer**, arXiv:2511.09448 2025 [[paper](https://arxiv.org/abs/2511.09448)]
1. **Survey Paper on AI Based Sports Highlight Generation for Social Media**, Journal of Scientific Research and Technology 2025 [[paper]( https://www.jsrtjournal.com/index.php/JSRT/article/view/194)]
1. **DIAMOND: an LLM-Driven Agent for Context-Aware Baseball Highlight Summarization**, REALM 2025 [[paper]( https://aclanthology.org/2025.realm-1.28/)]
1. **HIPPO-VIDEO: Simulating Watch Histories with Large Language Models for History-Driven Video Highlighting**, COLM 2025 [[paper](https://www.arxiv.org/abs/2507.16873)]
1. **SportSummarizer: a Unified Multimodal Fusion Transformer for Context-Aware Sports Video Summarization**, Neurocomputing 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S0925231225016832)]
1. **Tree-Of-Report: Table-to-Text Generation for Sports Game Reports with Tree-Structured Prompting**, ACL-SRW 2025 [[paper](https://openreview.net/pdf?id=gR4MPb03or)]
1. **Moneyball with LLMs: Analyzing Tabular Summarization in Sports Narratives**, arXiv:2510.18173 2025 [[paper](https://arxiv.org/abs/2510.18173)]
1. **SportsBuddy: Designing and Evaluating an AI-Powered Sports Video Storytelling Tool Through Real-World Deployment**, PacificVis 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11021035)]
1. **Experience Is All You Need: a Large Language Model Application of Fine-Tuned GPT-3.5 and RoBERTa for Aspect-Based Sentiment Analysis of College Football Stadium Reviews**, Sport Management Review 2025 [[paper]( https://www.tandfonline.com/doi/full/10.1080/14413523.2024.2386467?src=#abstract)]
1. **INVESTIGATING THE FACTORS INFLUENCING ADOPTION INTENTIONS OF CHATGPT FOR SPORT EVENTS**, SPORMETRE Beden Eğitimi ve Spor Bilimleri Dergisi 2025 [[paper]( https://dergipark.org.tr/tr/pub/spormetre/issue/92744/1606845)]
1. **BleacherBot: AI Agent as a Sports Co-Viewing Partner**, CHI 2025 [[paper]( https://dl.acm.org/doi/10.1145/3706598.3714178)]
1. **A System for Triggering Sports Instant Answers on Search Engines, SIGIR 2025** [[paper](https://dl.acm.org/doi/pdf/10.1145/3726302.3731953)]
1. **Assessing the Accuracy of Large Language Models in Extracting Latest Cricket Information**, Scientific Journal of Sport and Performance 2025 [[paper]( https://sjsp.aearedo.es/index.php/sjsp/article/view/accuracy-llms-extracting-cricket-data)]
1. **Agentic Generative AI for Media Content Discovery at the National Football League**, 2025 [[paper]( https://www.amazon.science/publications/agentic-generative-ai-for-media-content-discovery-at-the-national-football-league)]
1. **From Play to Replay: Composed Video Retrieval for Temporally Fine-Grained Videos**, arXiv:2506.05274 [[paper](https://arxiv.org/abs/2506.05274)]
1. **Korean Football in-Game Conversation State Tracking Dataset for Dialogue and Turn Level Evaluation**, Engineering Applications of Artificial Intelligence 2025 [[paper](https://www.sciencedirect.com/science/article/pii/S0952197624017305)]
1. **SoccerChat: Integrating Multimodal Data for Enhanced Soccer Game Understanding**, arXiv:2505.16630 [[paper]( https://arxiv.org/abs/2505.16630)]
1. **Multi-Agent System for Comprehensive Soccer Understanding**, arXiv:2505.03735 [[paper](https://arxiv.org/abs/2505.03735)]
1. **Towards Universal Soccer Video Understanding**, CVPR 2025 [[paper]( https://openaccess.thecvf.com/content/CVPR2025/html/Rao_Towards_Universal_Soccer_Video_Understanding_CVPR_2025_paper.html)]
1. **FineQuest: Adaptive Knowledge-Assisted Sports Video Understanding via Agent-of-Thoughts Reasoning**, MM 2025 [[paper]( https://arxiv.org/abs/2509.11796)]
1. **SPORTSQL: An Interactive System for Real-Time Sports Reasoning and Visualization**, arXiv:2508.17157 2025 [[paper](https://arxiv.org/abs/2508.17157)]
1. **Foresight in Sports Businesses: Exploring Emerging Scenarios Based on AI-Language Models and Financial Management Strategies**, Sports Business Journal 2025 [[paper]( https://sbj.alzahra.ac.ir/article_8629.html)]
1. **Comprehensive Site Selection Model for Sports Facilities in Iran: Leveraging AI Language Models**, Sport Management Journal 2025 [[paper]( https://jsm.ut.ac.ir/article_100786_46827a751b01ff496e97ba8034d9c9d3.pdf)]
1. **Leveraging LLMs and RAG for Enhanced Football Talent Scouting**, CAISE 2025 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-94931-9_24)]
1. **Footyintel: Creating an AI Scout for Better Talent Recognition**, International Journal of Environmental Sciences 2025 [[paper]( https://theaspd.com/index.php/ijes/article/view/1753)]
1. **Investigating Esports Tourism Research Using Artificial Intelligence Applications: ChatGPT Versus ZekAI**, Tourism and Recreation 2025 [[paper](https://dergipark.org.tr/tr/pub/tourismandrecreation/issue/93330/1517704)]
1. **AI-Powered ChatGPT in Sports Tourism Benefits, Challenges, and Future Prospects**, Redefining Tourism With AI and the Metaverse 2025 [[paper](https://www.igi-global.com/chapter/ai-powered-chatgpt-in-sports-tourism/372139)]
1. **SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models**, ICLR 2025 [[paper](https://openreview.net/forum?id=x1yOHtFfDh)]
1. **FSBench: A Figure Skating Benchmark for Advancing Artistic Sports Understanding**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_FSBench_A_Figure_Skating_Benchmark_for_Advancing_Artistic_Sports_Understanding_CVPR_2025_paper.html)]
1. **Sports Intelligence: Assessing the Sports Understanding Capabilities of Language Models Through Question Answering from Text to Video**, Electronics 2025 [[paper](https://www.mdpi.com/2079-9292/14/3/461)]
1. **FineBadminton: A Multi-Level Dataset for Fine-Grained Badminton Video Understanding**, MM 2025 [[paper](https://www.arxiv.org/abs/2508.07554)]
1. **SportR: A Benchmark for Multimodal Large Language Model Reasoning in Sports**, arXiv:2511.06499 2025 [[paper](https://arxiv.org/abs/2511.06499)]
1. **DeepSport: A Multimodal Large Language Model for Comprehensive Sports Video Reasoning via Agentic Reinforcement Learning**, arXiv:2511.12908 2025 [[paper](https://arxiv.org/abs/2511.12908)]
1. **Let's Play Across Cultures: A Large Multilingual, Multicultural Benchmark for Assessing Language Models' Understanding of Sports**, arXiv:2510.01247 2025 [[paper](https://arxiv.org/abs/2510.01247)]
1. **TennisTV: Do Multimodal Large Language Models Understand Tennis Rallies?**, arXiv:2509.15602 2025 [[paper](https://arxiv.org/abs/2509.15602)]
1.  **VideoVista: a Versatile Benchmark for Video Understanding and Reasoning**,arXiv 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/10982110)]
1.  **Video-SALMONN 2: Captioning-Enhanced Audio-Visual Large Language Models**, arXiv:2506.15220 [[paper](https://arxiv.org/abs/2506.15220)]
1.  **MMWorld: Towards Multi-Discipline Multi-Faceted World Model Evaluation in Videos**, ICLR 2025 [[paper](https://openreview.net/forum?id=tRNKe2Vgqt)]
1.  **LongVILA: Scaling Long-Context Visual Language Models for Long Videos**, ICLR 2025 [[paper](https://openreview.net/forum?id=wCXAlfvCy6)]
1.  **MLVU: Benchmarking Multi-Task Long Video Understanding**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_MLVU_Benchmarking_Multi-task_Long_Video_Understanding_CVPR_2025_paper.html)]
1.  **Video-MME: the First-Ever Comprehensive Evaluation Benchmark of Multi-Modal LLMs in Video Analysis**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Fu_Video-MME_The_First-Ever_Comprehensive_Evaluation_Benchmark_of_Multi-modal_LLMs_in_CVPR_2025_paper.pdf)]
1.  **MotionBench: Benchmarking and Improving Fine-Grained Video Motion Understanding for Vision Language Models**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Hong_MotionBench_Benchmarking_and_Improving_Fine-grained_Video_Motion_Understanding_for_Vision_CVPR_2025_paper.html)]
1.  **OVO-Bench: How Far Is Your Video-LLMs from Real-World Online Video Understanding?**  CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Niu_OVO-Bench_How_Far_is_Your_Video-LLMs_from_Real-World_Online_Video_CVPR_2025_paper.html)]
1.  **VISTA: Enhancing Long-Duration and High-Resolution Video Understanding by VIdeo SpatioTemporal Augmentation**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ren_VISTA_Enhancing_Long-Duration_and_High-Resolution_Video_Understanding_by_Video_Spatiotemporal_CVPR_2025_paper.html)]
1.  **HarmonySet: a Comprehensive Dataset for Understanding Video-Music Semantic Alignment and Temporal Synchronization**, CVPR 2025 [[paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_HarmonySet_A_Comprehensive_Dataset_for_Understanding_Video-Music_Semantic_Alignment_and_CVPR_2025_paper.html)]
1.  **VideoA11y-40K: a Large-Scale Dataset for Accessible Video Understanding** ,  CHI 2025 [[paper](https://dl.acm.org/doi/abs/10.1145/3706598.3714096)]
1.  **TUNA: Comprehensive Fine-Grained Temporal Understanding Evaluation on Dense Dynamic Videos**, ACL 2025 [[paper](https://aclanthology.org/2025.acl-long.91/)]
1.  **WorldSense: Evaluating Real-World Omnimodal Understanding for Multimodal LLMs**, arXiv:2502.04326 [[paper](https://arxiv.org/abs/2502.04326)]
1.  **V-STaR: Benchmarking Video-LLMs on Video Spatio-Temporal Reasoning**, arXiv:2503.11495 [[paper](https://arxiv.org/abs/2503.11495)]
1.  **MINERVA: Evaluating Complex Video Reasoning**, arXiv:2505.00681 [[paper](https://arxiv.org/abs/2505.00681)]
1.  **MAVERIX: Multimodal Audio-Visual Evaluation Reasoning IndeX**, arXiv:2503.21699 [[paper](https://arxiv.org/abs/2503.21699)]
1.  **RTV-Bench: Benchmarking MLLM Continuous Perception, Understanding and Reasoning Through Real-Time Video**, arXiv:2505.02064 [[paper](https://arxiv.org/abs/2505.02064)]
1.  **VidText: Towards Comprehensive Evaluation for Video Text Understanding**, arXiv:2505.22810 [[paper](https://arxiv.org/abs/2505.22810)]
1.  **SIV-Bench: a Video Benchmark for Social Interaction Understanding and Reasoning**, arXiv:2506.05425 [[paper](https://arxiv.org/abs/2506.05425)]
1.  **ExAct: a Video-Language Benchmark for Expert Action Analysis**, arXiv:2506.06277 [[paper](https://arxiv.org/abs/2506.06277)]
1.  **VRBench: a Benchmark for Multi-Step Reasoning in Long Narrative Videos**, arXiv:2506.10857 [[paper](https://arxiv.org/abs/2506.10857)]
1.  **Understanding and Benchmarking the Trustworthiness in Multimodal LLMs for Video Understanding**, arXiv:2506.12336 [[paper](https://arxiv.org/abs/2506.12336)]
1.  **CausalStep: a Benchmark for Explicit Stepwise Causal Reasoning in Videos**, arXiv:2507.16878 [[paper](https://arxiv.org/abs/2507.16878)]
1.  **EgoExoBench: a Benchmark for First- and Third-Person View Video Understanding in MLLMs**, arXiv:2507.18342 [[paper](https://arxiv.org/abs/2507.18342)]
1.  **WildVideo: Benchmarking LMMs for Understanding Video-Language Interaction**, IEEE Transactions on Pattern Analysis and Machine Intelligence 2025 [[paper](https://ieeexplore.ieee.org/abstract/document/11097075)]
1.  **ST-VLM: Kinematic Instruction Tuning for Spatio-Temporal Reasoning in Vision-Language Models**, arXiv:2503.19355 [[paper](https://arxiv.org/abs/2503.19355)]
1.  **Artificial intelligence in sport: A narrative review of applications, challenges and future trends**, Journal of Sports Sciences 2025 [[paper](https://www.tandfonline.com/doi/full/10.1080/02640414.2025.2518694)]
1.  **A Review of Artificial Intelligence in Sports: Applications, Ethical Concerns, and Legal Frameworks**, Research Square 2025 [[paper](https://www.researchsquare.com/article/rs-7182432/v1)]
1.  **Artificial intelligence in health and sport sciences: Promise, progress, and prudence**, Journal of Sport and Health Science 2025 [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12221458/)]
1.  **Using Large Language Models to Enhance Exercise Recommendations and Physical Activity in Clinical and Healthy Populations: Scoping Review**, JMIR Medical Informatics 2025 [[paper](https://medinform.jmir.org/2025/1/e59309/)]

### 2024

1. **Artificial Intelligence in Sport: Exploring the Potential of Using ChatGPT in Resistance Training Prescription**, Biology of sport 2024 [[paper](https://www.termedia.pl/Artificial-intelligence-in-sport-Exploring-the-potential-of-using-r-nChatGPT-in-resistance-training-prescription,78,51817,0,1.html )]
1. **Using Artificial Intelligence for Exercise Prescription in Personalised Health Promotion: a Critical Evaluation of OpenAI’s GPT-4 Model**, Biology of Sport 2024 [[paper](https://www.termedia.pl/Using-artificial-intelligence-for-exercise-prescription-in-personalised-health-promotion-A-critical-evaluation-of-OpenAI-s-GPT-4-model,78,52030,1,1.html)]
1. **ChatGPT and Exercise Prescription: Human vs. Machine or Human Plus Machine?**, Journal of Sport and Health Science 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S2095254623001060)]
1. **Infusing Behavior Science into Large Language Models for Activity Coaching**, PLOS Digital Health 2024 [[paper](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000431)]
1. **The Potential of Large Language Model Chatbots for Application to Epilepsy: Let’s Talk About Physical Exercise**, Epilepsy & Behavior Reports 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S2589986424000492)]
1. **Towards a Personal Health Large Language Model**, AIM-FM Workshop @ NeurIPS'24 Oral 2024 [[paper](https://openreview.net/forum?id=1Fbna6cNPw)]
1. **Optimizing Athletic Performance Through Advanced Nutrition Strategies: Can AI and Digital Platforms Have a Role in Ultraendurance Sports?**, Biology of Sport 2024 [[paper](https://www.termedia.pl/Optimizing-athletic-performance-through-advanced-nutrition-r-nstrategies-can-AI-and-digital-platforms-have-a-role-in-ultraendurance-sports-,78,54384,0,1.html)]
1. **MotionGPT-2: a General-Purpose Motion-Language Model for Motion Generation and Understanding**, arXiv:2410.21747 [[paper](https://arxiv.org/abs/2410.21747)]
1. **Who Could and Should Give Exercise Prescription: Physicians, Exercise and Health Scientists, Fitness Trainers, or ChatGPT?**, Journal of Sport and Health Science 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S2095254624000012)]
1. **Does ChatGPT Provide Comprehensive and Accurate Information Regarding the Effects, Types and Programming of Core Exercises?**, Turkish Journal of Kinesiology 2024 [[paper](https://dergipark.org.tr/en/pub/turkjkin/article/1516614)]
1. **ChatGPT Generated Training Plans for Runners Are Not Rated Optimal by Coaching Experts, but Increase in Quality with Additional Input Information**, Journal of sports science & medicine 2024 [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10915606/)]
1. **The Impact of LLM Hallucinations on Motor Skill Learning: a Case Study in Badminton**, IEEE Access 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10638024)]
1. **Assessment of Personalized Exercise Prescriptions Issued by ChatGPT 4.0 and Intelligent Health Promotion Systems for Patients with Hypertension Comorbidities Based on the Transtheoretical Model: A Comparative Analysis**, Journal of Multidisciplinary Healthcare 2024 [[paper](https://www.tandfonline.com/doi/full/10.2147/JMDH.S477452)]
1. **Assessing ChatGPT’s Competency in Addressing Interdisciplinary Inquiries on Chatbot Uses in Sports Rehabilitation: Simulation Study**, JMIR Medical Education 2024 [[paper](https://mededu.jmir.org/2024/1/e51157/)]
1. **Evaluating the Qualitative and Quantitative Performance of Generative AI on Knowledge in Sports Medicine: the Case of GPT**, General Aspects of Applying Generative AI in Higher Education: Opportunities and Challenges 2024 [[paper](https://link.springer.com/chapter/10.1007/978-3-031-65691-0_6)]
1. **Diagnostic Applications of AI in Sports: a Comprehensive Review of Injury Risk Prediction Methods**, Diagnostics 2024 [[paper](https://www.mdpi.com/2075-4418/14/22/2516)]
1. **Transforming Wearable Data into Personal Health Insights Using Large Language Model Agents**, arXiv:2406.06464 [[paper](https://arxiv.org/abs/2406.06464)]
1. **Large Language Models for Wearable Sensor-Based Human Activity Recognition, Health Monitoring, and Behavioral Modeling: a Survey of Early Trends, Datasets, and Challenges**, Sensors 2024 [[paper](https://www.mdpi.com/1424-8220/24/15/5045)]
1. **HARGPT: Are LLMs Zero-Shot Human Activity Recognizers?**, FMSys 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10590466)]
1. **LLaSA: Large Multimodal Agent for Human Activity Analysis Through Wearable Sensors**, arXiv 2024 [[paper](https://bashlab.wpi.edu/publications_pdf/imran2024llasa.pdf)]
1. **Rugby Scene Classification Enhanced by Vision Language Model**, CVPR 2024 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/html/Nonaka_Rugby_Scene_Classification_Enhanced_by_Vision_Language_Model_CVPRW_2024_paper.html)]
1. **ActionAtlas: a VideoQA Benchmark for Domain-Specialized Action Recognition**, NeurIPS 2024 [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f8643596721dbac71d67f89497323efe-Abstract-Datasets_and_Benchmarks_Track.html)]
1. **Smartboard: Visual Exploration of Team Tactics with LLM Agent**, IEEE Transactions on Visualization and Computer Graphics 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10670515)]
1. **Using Large Language Models to Generate Baseball Spray Charts in the Absence of Numerical Data, Proceedings of the Institution of Mechanical Engineers**, Part P: Journal of Sports Engineering and Technology 2024 [[paper](https://maloof.princeton.edu/sites/g/files/toruqf1016/files/documents/87Maloof.pdf)]
1. **Can Large Language Models Do Analytical Reasoning?**, arXiv:2403.04031  [[paper](https://arxiv.org/abs/2403.04031)]
1. **SportsMetrics: Blending Text and Numerical Data to Understand Information Fusion in LLMs**, ACL 2024 [[paper](https://aclanthology.org/2024.acl-long.17/)]
1. **Large Language Models on Race Commentary: Towards Granular Data in Cycling Analytics**, MLSA 2024 [[paper](https://link.springer.com/chapter/10.1007/978-3-031-86692-0_2)]
1. **When Reasoning Meets Information Aggregation: a Case Study with Sports Narratives**, EMNLP 2024 [[paper](https://aclanthology.org/2024.emnlp-main.246/)]
1. **A Stroke of Genius: Predicting the Next Move in Badminton**, CVPR 2024 CVsports Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/html/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.html)]
1. **Social Networks and Large Language Models for Division I Basketball Game Winner Prediction**, IEEE Access 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10535112/)]
1. **Using ChatGPT to Promote College Students’ Participation in Physical Activities and Its Effect on Mental Health**, World Journal of Psychiatry 2024 [[paper]( https://pmc.ncbi.nlm.nih.gov/articles/PMC10921293/)]
1. **Artificial Intelligence in Physical Education: Comprehensive Review and Future Teacher Training Strategies**, Frontiers in public health 2024 [[paper](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1484848/full)]
1. **X-VARS: Introducing Explainability in Football Refereeing with Multi-Modal Large Language Models**, CVPR 2024 Workshop [[paper](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/html/Held_X-VARS_Introducing_Explainability_in_Football_Refereeing_with_Multi-Modal_Large_Language_CVPRW_2024_paper.html)]
1. **MatchTime: Towards Automatic Soccer Game Commentary Generation**, EMNLP 2024 [[paper](https://aclanthology.org/2024.emnlp-main.99/)]
1. **Commentary Generation from Data Records of Multiplayer Strategy Esports Game**, NAACL 2024 Student Research Workshop [[paper](https://aclanthology.org/2024.naacl-srw.28/)]
1. **Personalized Video Comment Generation**, EMNLP Findings 2024 [[paper]( https://aclanthology.org/2024.findings-emnlp.979.pdf)]
1. **AiCommentator: a Multimodal Conversational Agent for Embedded Visualization in Football Viewing**, IUI 2024 [[paper]( https://dl.acm.org/doi/abs/10.1145/3640543.3645197)]
1. **SCBench: a Sports Commentary Benchmark for Video LLMs**,  arXiv:2412.17637 [[paper](https://arxiv.org/abs/2412.17637)]
1. **Designing for Automated Sports Commentary Systems**, IMX 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3639701.3656323)]
1. **LLM-Commentator: Novel Fine-Tuning Strategies of Large Language Models for Automatic Commentary Generation Using Football Event Data**, Knowledge-Based Systems 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S0950705124008530)]
1. **Large Scale Generative AI Text Applied to Sports and Music**,ACM SIGKDD 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3637528.3671542)]
1. **A Descriptive Basketball Highlight Dataset for Automatic Commentary Generation**, MM 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3664647.3681178)]
1. **AI-Based Sports Highlight Generation for Social Media**, MHV 2024 [[paper]( https://dl.acm.org/doi/abs/10.1145/3638036.3640799)]
1. **SNIL: Generating Sports News from Insights with Large Language Models**, IEEE Transactions on Visualization and Computer Graphics 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10507016/)]
1. **Advancing Cricket Narratives: AI-Enhanced Advanced Journaling in the IPL Using Language Models**, CONECCT 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10677234)]
1. **BADGE: BADminton Report Generation and Evaluation with LLM, IJCAI 2024 Workshop**,arXiv:2406.18116 [[paper]( https://arxiv.org/pdf/2406.18116v1)]
1. **Sportify: Question Answering with Embedded Visualizations and Personified Narratives for Sports Video**, IEEE Transactions on Visualization and Computer Graphics 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10673998)]
1. **Multimodal AI-Based Summarization and Storytelling for Soccer on Social Media**, MMSys 2024 [[paper](https://dl.acm.org/doi/abs/10.1145/3625468.3652197)]
1. **OneLove Beyond the Field - a Few-Shot Pipeline for Topic and Sentiment Analysis During the FIFA World Cup in Qatar**, KONVENS 2024 [[paper]( https://aclanthology.org/2024.konvens-main.35/)]
1. **Megan - a Sports Chatbot Using OpenAI APIs and Django Framework with Python**, International Conference for Convergence in Technology (I2CT) 2024 [[paper]( https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10543499&tag=1)]
1. **Querying Football Matches for Event Data: Towards Using Large Language Models**, ISACE 2024 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-69073-0_19)]
1. **Demo: Soccer Information Retrieval via Natural Queries Using SoccerRAG**, CBMI 2024 [[paper](https://ieeexplore.ieee.org/abstract/document/10859233)]
1. **SoccerRAG: Multimodal Soccer Information Retrieval via Natural Queries**, CBMI 2024 [[paper]( https://ieeexplore.ieee.org/abstract/document/10859209)]
1. **Enhancing Structured-Data Retrieval with GraphRAG: Soccer Data Case Study**, arxiv:2409.17580  [[paper](https://arxiv.org/abs/2409.17580)]
1. **Soccer-GraphRAG: Applications of GraphRAG in Soccer**, IRonGraphs 2024 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-71382-8_1)]
1. **Artificial Intelligence in Sport Scientific Creation and Writing Process**, Artificial Intelligence in Sports, Movement, and Health 2024 [[paper]( https://link.springer.com/chapter/10.1007/978-3-031-67256-9_2)]
1. **Human-Written vs AI-Generated Texts in Orthopedic Academic Literature: Comparative Qualitative Analysis**, JMIR formative research 2024 [[paper]( https://formative.jmir.org/2024/1/e52164)]
1. **A Financial Management Maturity Model in Sports Organizations: a Novel Approach Using Artificial Intelligence**, JNSSM 2024 [[paper]( https://jnssm.uk.ac.ir/article_4546_f005ba1018dbf2a9a6984bed3c087ac0.pdf)]
1. **From PDFs to Structured Data: Utilizing LLM Analysis in Sports Database Management**, arXiv:2410.17619 [[paper]( https://arxiv.org/abs/2410.17619)]
1. **Empowering the Sports Scientist with Artificial Intelligence in Training, Performance, and Health Management**, Sensors 2024 [[paper]( https://www.mdpi.com/1424-8220/25/1/139)]
1. **Sports-QA: A Large-Scale Video Question Answering Benchmark for Complex and Professional Sports** [[paper](https://arxiv.org/abs/2401.01505)]
1. **SportQA: A Benchmark for Sports Understanding in Large Language Models**, NAACL 2024 [[paper](https://aclanthology.org/2024.naacl-long.283/)]
1.  **InternVid: a Large-Scale Video-Text Dataset for Multimodal Understanding and Generation**, ICLR 2024 [[paper](https://openreview.net/forum?id=MLBdiWu4Fw)]
1.  **E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding**, NeurIPS 2024 [[paper](https://openreview.net/forum?id=KoSSEp6Du5)]
1.  **Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives**, CVPR 2024 [[paper](https://openaccess.thecvf.com/content/CVPR2024/html/Grauman_Ego-Exo4D_Understanding_Skilled_Human_Activity_from_First-_and_Third-Person_Perspectives_CVPR_2024_paper.html)]
1.  **LVBench: an Extreme Long Video Understanding Benchmark**, arXiv:2406.08035 [[paper](https://arxiv.org/abs/2406.08035)]
1.  **FIOVA: a Multi-Annotator Benchmark for Human-Aligned Video Captioning**, arXiv:2410.15270 [[paper](https://arxiv.org/abs/2410.15270)]
1.  **Neptune: the Long Orbit to Benchmarking Long Video Understanding**, arXiv:2412.09582 [[paper](https://arxiv.org/abs/2412.09582)]
1.  **Enhancing Multimodal LLM for Detailed and Accurate Video Captioning Using Multi-Round Preference Optimization**, arXiv:2410.06682 [[paper](https://arxiv.org/abs/2410.06682)]
1.  **Language and Multimodal Models in Sports: A Survey of Datasets and Applications**, arXiv:2406.12252 [[paper](https://arxiv.org/abs/2406.12252)]
1.  **Impact of ChatGPT Technology on Sports Industry**, Journal of New Media and Economics (JNME) 2024 [[paper](http://www.stemmpress.com/jnme/jnme20244/1452.html)]
1.  **Sport and the Promise of Artificial Intelligence: Human and Machine Futures**, Sociology of Sport Journal 2024 [[paper](https://journals.humankinetics.com/view/journals/ssj/aop/article-10.1123-ssj.2024-0150/article-10.1123-ssj.2024-0150.xml)]
1.  **A deep introspection into the role of ChatGPT for transforming hospitality, leisure, sport, and tourism education**, Journal of Hospitality, Leisure, Sport & Tourism Education 2024 [[paper](https://www.sciencedirect.com/science/article/pii/S1473837624000273)]
1.  **Challenges and opportunities of artificial intelligence implementation within sports science and sports medicine teams**, Frontiers in Sports and Active Living 2024 [[paper](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1332427/full)]

### 2023

1. **MAAIG: Motion Analysis and Instruction Generation**, MM Asia 2023 [[paper](https://arxiv.org/abs/2311.00980)]
1. **The Role of ChatGPT in Sports Trauma: a Mini Review on Strengths and Limits of Open AI Application**, Discover Artificial Intelligence 2023 [[paper](https://link.springer.com/article/10.1007/s44163-023-00093-1)]
1. **Interdisciplinary Inquiry via PanelGPT: Application to Explore Chatbot Application in Sports Rehabilitation**, medRxiv 2023 [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10402232/)]
1. **Artificial Intelligence in Sports Medicine: Could GPT-4 Make Human Doctors Obsolete?**, Annals of Biomedical Engineering 2023 [[paper](https://link.springer.com/article/10.1007/s10439-023-03213-1)]
1. **Artificial Intelligence and ChatGPT in Orthopaedics and Sports Medicine**, Journal of Experimental Orthopaedics 2023 [[paper](https://link.springer.com/article/10.1186/s40634-023-00642-8)]
1. **Chatbot Generative Pre-Trained Transformer and Artificial Intelligence in Sports Physical Therapy and Rehabilitation**, Saudi Journal of Sports Medicine 2023 [[paper](https://journals.lww.com/sjsm/fulltext/2023/23020/chatbot_generative_pre_trained_transformer_and.6.aspx)]
1. **ChatGPT Is a Breakthrough in Science and Education but Fails a Test in Sports and Exercise Psychology**, Baltic Journal of Sport and Health Sciences 2023 [[paper](https://journals.lsu.lt/baltic-journal-of-sport-health/article/view/1341)]
1. **Increasing Physical Activity Using an Just-in-Time Adaptive Digital Assistant Supported by Machine Learning: a Novel Approach for Hyper-Personalised mHealth Interventions**, Journal of Biomedical Informatics 2023 [[paper]( https://www.sciencedirect.com/science/article/pii/S1532046423001569)]
1. **TacticalGPT: Uncovering the Potential of LLMs for Predicting Tactical Decisions in Professional Football**, StatsBomb Conference 2023 [[paper](https://blogarchive.statsbomb.com/uploads/2023/10/TacticalGPT-Uncovering-the-Potential-of-LLMs-for-Predicting-Tactical-Decisions-in-Professional-Football.pdf)]
1. **Proactive Autonomous Assignments as Pedagogical Responses to the Rise of Artificial Intelligence Solutions in Sport Management Teaching Practice**, Sport Management Education Journal 2023 [[paper](https://journals.humankinetics.com/view/journals/smej/19/1/article-p54.xml)]
1. **Artificial Intelligence in Sport Management Education: Playing the AI Game with ChatGPT, Journal of Hospitality**, Leisure, Sport & Tourism Education 2023 [[paper](https://www.sciencedirect.com/science/article/pii/S1473837623000400)]
1. **Artificial Intelligence in Physical Education and Sports: New Horizons with ChatGPT**, Mediterranean Journal of Sport Science 2023 [[paper](https://dergipark.org.tr/en/pub/asbid/issue/80422/1291604)]
1. **Soccer Artificial Intelligence Commentary Service on the Base of Video Analytic and Large Language Models**, TELFOR 2023 [[paper]( https://ieeexplore.ieee.org/abstract/document/10372671)]
1. **Multi-Modal Architecture for Cricket Highlights Generation: Using Computer Vision and Large Language Model**, ICOSST 2023 [[paper](https://ieeexplore.ieee.org/abstract/document/10414235/)]
1. **Generating Factually Consistent Sport Highlights Narrations**, MMSports 2023 [[paper]( https://dl.acm.org/doi/abs/10.1145/3606038.3616157)]
1. **Esports Debut as a Medal Event at 2023 Asian Games: Exploring Public Perceptions with BERTopic and GPT-4 Topic Fine-Tuning**, arXiv:2409.18798 [[paper]( https://arxiv.org/abs/2409.18798)]
1. **FootGPT : a Large Language Model Development Experiment on a Minimal Setting**, arXiv:2308.08610 [[paper]( https://arxiv.org/abs/2308.08610)]
1. **ChatGPT for Sample-Size Calculation in Sports Medicine and Exercise Sciences: a Cautionary Note**, International Journal of Sports Physiology and Performance 2023 [[paper](https://journals.humankinetics.com/view/journals/ijspp/18/10/article-p1219.xml)]
1. **AI Did Not Write This Manuscript, or Did It? Can We Trick the AI Text Detector into Generated Texts? the Potential Future of ChatGPT and AI in Sports & Exercise Medicine Manuscript Generation**, BMJ Open Sport & Exercise Medicine 2023 [[paper](https://bmjopensem.bmj.com/content/9/1/e001568)]
1. **From Human Writing to Artificial Intelligence Generated Text: Examining the Prospects and Potential Threats of ChatGPT in Academic Writing**, Biology of sport 2023 [[paper](https://www.termedia.pl/From-human-writing-to-artificial-intelligence-generated-text-examining-the-prospects-and-potential-threats-of-ChatGPT-in-academic-writing,78,50268,0,1.html)]
1. **QASports: A Question Answering Dataset about Sports**, Dataset Showcase Workshop (DSW) 2023 [[paper](https://sol.sbc.org.br/index.php/dsw/article/view/25500)]
1. **Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models**, TMLR 2023 [[paper](https://openreview.net/forum?id=uyTL5Bvosj&nesting=2&sort=date-desc)]
1.  **Large Language Models in Sport Science & Medicine: Opportunities, Risks and Considerations**, arXiv 2023 [[paper](https://arxiv.org/abs/2305.03851)]

### 2022

1. **Soccer Game Summarization Using Audio Commentary, Metadata, and Captions**, NarSUM 2022 [[paper](https://dl.acm.org/doi/abs/10.1145/3552463.3557019)]
1. **Knowledge Enhanced Sports Game Summarization**, WSDM 2022 [[paper]( https://dl.acm.org/doi/abs/10.1145/3488560.3498405)]
1. **Sporthesia: Augmenting Sports Videos Using Natural Language**, IEEE transactions on visualization and computer graphics 2022 [[paper]( https://ieeexplore.ieee.org/abstract/document/9911988/)]

### 2021

1. **SportsSum2.0: Generating High-Quality Sports News from Live Text Commentary**, CIKM 2021 [[paper]( https://dl.acm.org/doi/abs/10.1145/3459637.3482188)]

### 2020

1. **Predicting in-Game Actions from Interviews of NBA Players**, Computational Linguistics 2020 [[paper](https://direct.mit.edu/coli/article/46/3/667/93377/Predicting-In-Game-Actions-from-Interviews-of-NBA)]

<!-- YEAR_INDEX:END -->

## 🤝 Contribution

This is a living collection. If we missed a relevant paper, dataset, benchmark, or project, please read the [contribution guide](CONTRIBUTING.md), then use the [paper request form](https://github.com/Road2Redemption/Awesome_Large_Models_In_Sports1/issues/new?template=add-paper.yml) or open a pull request.

Add new works only to the most relevant taxonomy section using this format:

```markdown
1. **Paper Title**, Venue Year [[paper](https://link-to-paper)]
```

Please use an official publication page, DOI, ACL Anthology, OpenReview, or arXiv link whenever possible. Automated checks validate entry structure, duplicate links, local assets, and citation metadata on every pull request.

## 📚 Citation

If you find this repository useful for your research or work, please consider citing our paper:

You can also download the citation as [`paper.bib`](paper.bib) or use GitHub's **Cite this repository** button.

```bibtex
@inproceedings{xu-etal-2026-survey,
  title     = {A Survey of Large Models in Sports},
  author    = {Xu, Yichen and Ma, Jianzhe and Wang, Chuhan and Cao, Zhonghao and Chen, Liangyu and Wang, Wenxuan and Jin, Qin},
  editor    = {Liakata, Maria and Moreira, Viviane P. and Zhang, Jiajun and Jurgens, David},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2026},
  month     = jul,
  year      = {2026},
  address   = {San Diego, California, United States},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2026.findings-acl.1851/},
  doi       = {10.18653/v1/2026.findings-acl.1851},
  pages     = {37154--37189}
}
```

If this survey or repository helps your work, please consider citing the paper and starring the repository so that more researchers can discover this growing area.
