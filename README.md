# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/mvp-projects/easy-cloud-publish/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                              |    Stmts |     Miss |   Branch |   BrPart |     Cover |   Missing |
|------------------------------------------------------------------ | -------: | -------: | -------: | -------: | --------: | --------: |
| easy\_cloud\_publish/\_\_init\_\_.py                              |        0 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/cli/\_\_init\_\_.py                          |        2 |        2 |        0 |        0 |      0.0% |       1-3 |
| easy\_cloud\_publish/cli/image/\_\_init\_\_.py                    |        0 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/cli/image/cli.py                             |       23 |       23 |        4 |        0 |      0.0% |      3-51 |
| easy\_cloud\_publish/cli/root.py                                  |        5 |        5 |        0 |        0 |      0.0% |      2-12 |
| easy\_cloud\_publish/core/\_\_init\_\_.py                         |        0 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/services/\_\_init\_\_.py                |        0 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/services/docker/\_\_init\_\_.py         |        2 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/services/docker/client.py               |        8 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/services/docker/clients/\_\_init\_\_.py |        0 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/services/docker/clients/base.py         |        6 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/services/docker/clients/image.py        |       21 |        0 |        4 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/services/docker/exceptions.py           |        5 |        0 |        0 |        0 |    100.0% |           |
| easy\_cloud\_publish/core/use\_cases/\_\_init\_\_.py              |        2 |        2 |        0 |        0 |      0.0% |       1-3 |
| easy\_cloud\_publish/core/use\_cases/build\_image.py              |       28 |       28 |        6 |        0 |      0.0% |      2-57 |
| easy\_cloud\_publish/core/use\_cases/deploy\_image.py             |        0 |        0 |        0 |        0 |    100.0% |           |
|                                                         **TOTAL** |  **102** |   **60** |   **14** |    **0** | **39.7%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/mvp-projects/easy-cloud-publish/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/mvp-projects/easy-cloud-publish/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/mvp-projects/easy-cloud-publish/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/mvp-projects/easy-cloud-publish/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fmvp-projects%2Feasy-cloud-publish%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/mvp-projects/easy-cloud-publish/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.