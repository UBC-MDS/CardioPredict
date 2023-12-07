# CHANGELOG

This document outlines the improvements and changes made to the project, particularly in response to feedback. Each entry includes references to specific lines of code, commit messages, pull requests, etc., providing clear evidence of these enhancements.

---

## [Release 1.0.0] - 2023-11-18

### Feedback on Milestone 1 ([issue #21](https://github.com/UBC-MDS/CardioPredict/issues/21))

Following up on the feedback from Grapescope for Milestone 1, this issue serves as a checklist to guide our revisions for Milestone 3. Let's ensure we address the necessary and related points (prioritized by the number of stars) to avoid repeating any deductions.

1. organization and structure (***Grading comment:The analysis notebook ( *.ipynb or * .Qmd or *Rmd) should be in a sub-directory called something sensible, such as analysis, src, notebooks, docs, etc, to aid in the discoverability of this file, and related ones. Having too many files in the project root makes the project organization less understandable and can lead to longer activation times to productivity for collaborators (including future you!).)
2. readme.md(***Grading comment: Links are broken or send user to incorrect location or missing links)
3. code_of_conduct(*Grading comment:Spelling or grammatical errors. Fail to clearly cite the reference (missing info or links).)
4. environment.yml (***Grading comment:Programming language and/or package versions are pinned using >= instead of =. This means that each time the environment is built in the future, the most recent version of the programming language and/or package will be installed in the environment. This will lead to the environment not being able to be reproducibly built in the future.)
5. license.md(*Grading comment:No Creative Commons license (for project report) was specified.)
6. methods (**Grading comment:Important methodology descriptions missing (e.g., did not explain in narrative what metric was being used for model parameter optimization).)
7. results(**Grading comment:Information in tables are not clearly presented.)
8. spelling and grammer (*There were just a couple spelling or grammatical errors. They did not impact the understanding of the document.)
9. follow GitHub flow version control workflow (***Grading comment: Division of work on many branches is not ideal (branches are too big - they should be small independent units of work)."

### Added🆕

- Feedback #3: In response to feedback highlighting spelling and grammatical errors, and the lack of clear citations, we have thoroughly reviewed and updated our Code of Conduct. These revisions ensure clarity and accuracy, with specific attention to referencing. The updated document can be viewed in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/0369a9682fda6d6d9f020e553d5523c22eb60a83) and the updated version can be found [here](https://github.com/UBC-MDS/CardioPredict/blob/main/CODE_OF_CONDUCT.md).
- Feedback #5: Addressing the oversight pointed out in the grading comments, we have now added a Creative Commons license to our project with repo link added. This addition clearly delineates the usage rights and restrictions for our project report, aligning with open-source best practices. The license details are specified in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/b4a228a1bddac02d0d4125b4ac00d49c8f11c4e1), and the updated version can be found [here](https://github.com/UBC-MDS/CardioPredict/blob/main/LICENSE).
- Feedback #6: To rectify the gaps in our methodology narrative, particularly concerning the metrics used for model parameter optimization, we have expanded the methods section of our final report. This comprehensive description now includes detailed explanations of our approach to model tuning and the rationale behind our choice of metrics. These amendments are documented in [Commit](https://github.com/UBC-MDS/CardioPredict/commit/a90ec4c1bb307e7bb796078e79114b1a3fe2eeb5).
- Feedback #7: Following feedback regarding the unclear presentation of information in our results tables, we have undertaken a comprehensive revision of this section. The tables have been reformatted for enhanced readability and comprehension, ensuring that key findings are presented in a clear, concise, and visually accessible manner. These changes are encapsulated in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/a90ec4c1bb307e7bb796078e79114b1a3fe2eeb5) and the final report can be found [here](https://ubc-mds.github.io/CardioPredict/heart_analysis_report.html).

### Changed🔄

* Feedback #1: we have restructured the repository for enhanced efficiency in Mileston 2 [Release 1.0.2] . This involved relocating the analytical notebooks and corresponding HTML outputs to the 'src' sub-directory, which has been done in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/baaa36f7084ff45bdde7db7b54eab5c915ab8c1e). Further details of this modification are documented in [Issue #13](https://github.com/UBC-MDS/CardioPredict/issues/13).
* Feedback # 9: In response to the feedback on our version control workflow, particularly regarding the oversized branches, we have restructured our approach to adhere more closely to GitHub Flow principles. We now ensure that useless and irrelated branches have been removed, and remaining branches are independent unit of work, facilitating better organization and efficiency. The active branches are listed [here](https://github.com/UBC-MDS/CardioPredict/branches/active).

### Fixed🐛

- Feedback #2: We have addressed the issue of broken or incorrect links in our `README.md` file. All links have been thoroughly checked and updated to ensure they direct users to the correct locations, and any previously missing links have been added in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/efd99be1bd3195ac46b2d93a5d4af98b749d59c7). Please find the [updated version](https://github.com/UBC-MDS/CardioPredict/blob/main/README.md).
- Feedback #4: To ensure reproducibility in the future, we have modified our `environment.yml` file, replacing the use of `>=` with `=` for pinning programming language and package versions. The updated yml file can be found [here](https://github.com/UBC-MDS/CardioPredict/blob/main/environment.yaml).
- Feedback #8: Minor spelling and grammatical errors, previously present in our final report have been meticulously corrected. The changes can be reviewed in the [final report](https://ubc-mds.github.io/CardioPredict/heart_analysis_report.html). (need a link))

### Enhancement🚀

- To streamline our repository management, we have added a `.gitignore` file, ensuring unnecessary files such as `__pycache__` folders, generated during `pytest` executions, are not tracked by Git. This addition aids in keeping our repository clean and focused only on relevant files. The implementation of this cleanup strategy can be viewed in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/ede97e1d51f64d680dfa98484554206b02bde01a).

## [Release 1.0.2] - 2023-11-18

### Feedback on Milestone 2 ([issue #39](https://github.com/UBC-MDS/CardioPredict/issues/39))

Following up on the feedback from Grapescope for Milestone 2, this issue serves as a checklist to guide our revisions for Milestone 4. Let's ensure we address the necessary and related points.

1. Add examples to the functions 'run_knn_analysis.py, logistic_regression_evaluation.py, and create_pairwise_scatter_plot.py'
2. Add tests for 'test_split.py', specifically create an edge-case input, e.g., where the paths are empty or not in the correct format
3. In logistic_regression_evaluation.py, it's better to use a Python dictionary with meaningful key names to return, instead of a tuple in which the output is based on order. (not as clear and meaningful)

### Added🆕

- Feedback 1: added examples to the functions of 'run_knn_analysis.py', 'logistic_regression_evaluation.py', and 'create_pairwise_scatter_plot.py' and 'read_csv.py', see [commit](https://github.com/UBC-MDS/CardioPredict/commit/b8513ceebf76f5e88d666ca81003123dfe86239b), [commit](https://github.com/UBC-MDS/CardioPredict/commit/49a120107e0da0d55209867e172c47f0eb3ce59a),[ commit](https://github.com/UBC-MDS/CardioPredict/commit/d58beab775082c69dcaace111ceaf962958c0811) and [commit](https://github.com/UBC-MDS/CardioPredict/commit/f4590fe9d89e766894099618c73a1e613c8d0575).
- Feedback 2: added an edge-case input where there paths are empty or not in the correct format into the 'test_split.py', see [commit](https://github.com/UBC-MDS/CardioPredict/commit/0b3db6e4622c69af3cfc37c01663afde339e34ab).

### Changed🔄

- Feedback 3:. changed to use a Python dictionary with meaningful key names to return, instead of a tuple in which the output is based on order. Details in [commit](https://github.com/UBC-MDS/CardioPredict/commit/49a120107e0da0d55209867e172c47f0eb3ce59a).

### Removed🗑️

- Feedback #2: 'test_split.py' is a testing function which was put into a wrong folder, and the misplaced one has been removed. Refer to [commit](https://github.com/UBC-MDS/CardioPredict/commit/4a860973169b23f3997f8b369f1235d177ba8978).

## [Release 2.0.0] - 2023-12-03

### Team Internal Review ([issue #37](https://github.com/UBC-MDS/CardioPredict/issues/37))

Afterwards the submission of Milestone 3, this issue serves as a checklist of team internal review for improving the clarity, fixing bugs and typos, enhancing writing quality and streamling work flow.

**Bugs and typos:**

1. [X] Citation (Tsao 2015) missing tags in data section

**Writing quality:**

* [X] Rewrite abstract to make more appealing to audience in this [commit](https://github.com/UBC-MDS/CardioPredict/commit/b0aebb5ce828446802c9ffb56355f220f147b53c)

**Clarity and explaining:**

* [X] We need a research paper title, so far we use a project title as a paper title

**Workflow and version control:**

* [X] Clean up and discard useless branches

### Feedback from Peer Review ([issue #36](https://github.com/UBC-MDS/CardioPredict/issues/36))

#### Review Comments: @shawnhu444

This project exemplifies a highly standardized approach to data analysis and software development, aligning with best practices in several key areas:

1. High code quality, functionality documentation and follow the community guidelines. These aspects are vital for maintaining and scaling the software efficiently, ensuring its long-term viability.
2. The code submitted ensures data accessibility by providing a complete computational methods and putting details, functions. These features significantly enhance the reproducibility and reliability of the research, which are cornerstones of scientific rigor.
3. Reporting: The comprehensive approach to reporting, including clear articulation of research questions, background, functions, and coupled with high-quality writing and complete referencing .This demonstrates an exemplary standard in code communication.

In summary, this project stands out for comprehensive documentation, code quality, reproducibility, and thorough analysis reporting.

#### Review Comments: @sungg888

1. Documentation: The project is good with its detailed documentation, easy installation, and usage examples. The inclusion of community guidelines significantly aids collaboration and user support.
2. Code Quality: The code is well-organized, readable, and adheres to style guidelines, enhancing its maintainability. The project also have clear and readable robust testing framework to test its reliability.
3. Reproducibility: The project excels in reproducibility, providing accessible raw data, comprehensive computational methods, and clear steps in Readme.
   Analysis Report: The analysis report is clear and detailed, effectively communicating the research question, methods, and results. The high-quality writing makes the report engaging and informative. The report covers all points in the rubric.
4. Overall, the project is a high-quality, reproducible research. And it meet the standards of review checklist.

#### Review Comments: @Rachel0619

Overall, the project is conducted in high-quality and I'm deeply impressed by your hard work.

I really appreciate the plotting part of the report. The figures are well made and organized.

1. *Due to some reasons, after I git cloned the repo and ran docker compose up in the root folder, there's an error says: Error response from daemon: driver failed programming external connectivity on endpoint cardiopredict-disease_pred-1 (ca65c7817f322d11658c165784b27d8b6e5054acd8caa3412341e3be17081da4): Bind for 0.0.0.0:8888 failed: port is already allocated
   I have built the image successfully but not able to see the url starting with 127. Maybe double check with the reproducibility. This might not be a problem on your machine., just double check though.*
2. *Low recall might be an issue in the context of early detection and intervention a disease (if this is the research question of this project). You might want to try some other classification models to see if you can get higher recall.*
3. *The src file is a little bit messy now with different type of files in it.*

#### Review Comments: @carrieyanyi

Please provide more detailed feedback here on what was done particularly well, and what could be improved. It is especially important to elaborate on items that you were not able to check off in the list above.

I really enjoy going through this project and gain some knowledge about Cardiovascular Disease. The overall structure of the project is well organized. Both figures and models have sufficient descriptions.

1. *Installation:
   Some issues were encountered when i runned the script.
   EDA.py: "ValueError: Saving charts in 'png' format requires the vl-convert-python or altair_saver package: see [http://github.com/altair-viz/altair_saver/](https://github.com/altair-viz/altair_saver/)"*
2. *Reference: In the Data section, the citation for Tsao201 is mis-spelling, it should be Tsao2015 instead.*
3. *Visualization: It would be more obvious to add legend explanation in figure 5 to different what does disease 0 and 1 mean.*
4. *Abbreviation: A lot of terminology are used in the report, it would be great if maintaining consistency in the use of abbreviations, rather than alternating with their full names.*

### Added🆕

- **Reivew 1 from @carrieyanyi. See [commit](URL).**

### Changed🔄

- **Reivew 3 from @carrieyanyi. Details in [commit](URL).**

### Fixed🐛

- Review 1 from @Rachel0619: Fixed docker-compose.yml file with updated tag . Relevant changes in [commit](https://github.com/UBC-MDS/CardioPredict/commit/31203faa08c9d38e88504643c743b6ed02d2f534).
- Reivew 2 from @carrieyanyi: Fixed the missing tag in citation Tsao2015 in this [commit](https://github.com/UBC-MDS/CardioPredict/commit/70c89c1dabf2fb8ee45f1ff51a0becdb50dd893a).
- **Reivew 4 from @carrieyanyi:**

### Removed🗑️

- Review 3 from @Rachel0619: Removed unrelated .ipynb files under [/src](https://github.com/UBC-MDS/CardioPredict/tree/main/src) directory. Refer to [commit](https://github.com/UBC-MDS/CardioPredict/commit/563ac281bd980702df6de06ee863b323b8f593ef).

### Enhancement🚀

* Review 2 from @Rachel0619: Add limitations in the discussion section to discuss the potential reasons that might lead to this moderate accuracy and recall. Refer to [commit](https://github.com/UBC-MDS/CardioPredict/commit/563ac281bd980702df6de06ee863b323b8f593ef).

## Notes

- Each entry in this log is intended to make tracking changes and their reasons transparent and straightforward.
- The log is maintained consistently to ensure that every significant modification, addition, or removal is documented for easy reference.
