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
- Feedback #6: To rectify the gaps in our methodology narrative, particularly concerning the metrics used for model parameter optimization, we have expanded the methods section of our final report. This comprehensive description now includes detailed explanations of our approach to model tuning and the rationale behind our choice of metrics. These amendments are documented in [Commit](https://github.com/UBC-MDS/CardioPredict/commit/f1f77a2cc0df52cd170f765decc9610e37acadc5).
- Feedback #7: Following feedback regarding the unclear presentation of information in our results tables, we have undertaken a comprehensive revision of this section. The tables have been reformatted for enhanced readability and comprehension, ensuring that key findings are presented in a clear, concise, and visually accessible manner. These changes are encapsulated in [this commit]() and were further elaborated in [Pull Request](). (need a link here)

### Changed🔄

* Feedback #1: we have restructured the repository for enhanced efficiency in Mileston 2 [Release 1.0.2] . This involved relocating the analytical notebooks and corresponding HTML outputs to the 'src' sub-directory, which has been done in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/baaa36f7084ff45bdde7db7b54eab5c915ab8c1e). Further details of this modification are documented in [Issue #13](https://github.com/UBC-MDS/CardioPredict/issues/13).
* Feedback # 9: In response to the feedback on our version control workflow, particularly regarding the oversized branches, we have restructured our approach to adhere more closely to GitHub Flow principles. We now ensure that useless and irrelated branches have been removed, and remaining branches are independent unit of work, facilitating better organization and efficiency. This workflow adjustment is detailed in [this commit](). (need a link)

### Fixed🐛

- Feedback #2: We have addressed the issue of broken or incorrect links in our `README.md` file. All links have been thoroughly checked and updated to ensure they direct users to the correct locations, and any previously missing links have been added in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/efd99be1bd3195ac46b2d93a5d4af98b749d59c7). Please find the [updated version](https://github.com/UBC-MDS/CardioPredict/blob/main/README.md).
- Feedback #4: To ensure reproducibility in the future, we have modified our `environment.yml` file, replacing the use of `>=` with `=` for pinning programming language and package versions. The updated yml file can be found [here](https://github.com/UBC-MDS/CardioPredict/blob/main/environment.yaml).
- Feedback #8: Minor spelling and grammatical errors, previously present in our final report have been meticulously corrected. The changes can be reviewed in the [final report](). (need a link))

### Enhancement🚀

- To streamline our repository management, we have added a `.gitignore` file, ensuring unnecessary files such as `__pycache__` folders, generated during `pytest` executions, are not tracked by Git. This addition aids in keeping our repository clean and focused only on relevant files. The implementation of this cleanup strategy can be viewed in [this commit](https://github.com/UBC-MDS/CardioPredict/commit/ede97e1d51f64d680dfa98484554206b02bde01a).



## [Release 1.0.2] - 2023-11-18

### Feedback on Milestone 2

### Added🆕

- New feature or file added, addressing feedback on [issue/topic]. See [commit](URL) or [pull request](URL).

### Changed🔄

- Modified [filename/code component] for better performance, as suggested in [feedback source]. Details in [commit](URL).

### Fixed🐛

- Fixed [specific bug or issue] as per [feedback source]. Relevant changes in [pull request](URL) or [commit](URL).

### Removed🗑️

- Removed [obsolete feature or file], following suggestions from [feedback source]. Refer to [commit](URL).

### Security🔒

- Improved security measures as highlighted in [feedback]. Implemented in [commit](URL).

## [Release 2.0.0] - 2023-12/02

### Feedback from Peer Review

### Added🆕

- New feature or file added, addressing feedback on [issue/topic]. See [commit](URL) or [pull request](URL).

### Changed🔄

- Modified [filename/code component] for better performance, as suggested in [feedback source]. Details in [commit](URL).

### Fixed🐛

- Fixed [specific bug or issue] as per [feedback source]. Relevant changes in [pull request](URL) or [commit](URL).

### Removed🗑️

- Removed [obsolete feature or file], following suggestions from [feedback source]. Refer to [commit](URL).

### Enhancement🚀

### Security🔒

- Improved security measures as highlighted in [feedback]. Implemented in [commit](URL).



## Notes

- Each entry in this log is intended to make tracking changes and their reasons transparent and straightforward.
- The log is maintained consistently to ensure that every significant modification, addition, or removal is documented for easy reference.
