<p align="center"><img src="/misc/travis-ci.gif"><img src="/misc/github.gif" height=325 width=375></p>

---
 
 
| &nbsp;[![Travis](https://img.shields.io/travis/ajaymache/travis-ci-with-github.svg)](https://travis-ci.org/ajaymache/travis-ci-with-github)&nbsp;&nbsp; | &nbsp;&nbsp;[![license](https://img.shields.io/github/license/ajaymache/travis-ci-with-github.svg)](https://opensource.org/licenses/MIT)&nbsp;&nbsp; | &nbsp;&nbsp;[![GitHub issues](https://img.shields.io/github/issues/ajaymache/travis-ci-with-github.svg?colorB=DAA520)](https://github.com/ajaymache/travis-ci-with-github/issues)&nbsp;&nbsp; | &nbsp;&nbsp;[![GitHub language count](https://img.shields.io/github/languages/count/ajaymache/travis-ci-with-github.svg?colorB=ff5733)](https://github.com/ajaymache/travis-ci-with-github)&nbsp;&nbsp; | &nbsp;&nbsp;[![GitHub contributors](https://img.shields.io/github/contributors/ajaymache/travis-ci-with-github.svg?colorB=008080)](https://GitHub.com/ajaymache/travis-ci-with-github/graphs/contributors/)&nbsp;&nbsp; | &nbsp;&nbsp;![Contributions](/shields/contributions.svg)&nbsp;&nbsp; |
|-------|---------|---------|---------|---------|---------|

---

### About
This repository aims at getting started with **[Travis CI](https://travis-ci.org)** for your **[Github](https://github.com)** repositories. For demonstration purposes a very simple package is created with some test cases to explain how to integrate **Travis CI** for continous integration with **Github**.

### What is Travis CI?
Travis CI is a hosted, distributed continuous integration service used to build and test software projects hosted at GitHub.
Open source projects may be tested at no charge via [https://travis-ci.org](https://travis-ci.org). Private projects may be tested at [https://travis-ci.com](https://travis-ci.com) on a fee basis. TravisPro provides custom deployments of a proprietary version on the customer's own hardware. (**Source** - [Wikipedia](https://en.wikipedia.org/wiki/Travis_CI))

### Getting started
- The folder **pkg** contains a arithmetic package which has been created for demonstration puposes. The folder **pkg** has 2 sub-folders **arithmetic** and **testing** with files **arithmetic.py** and **testing.py**.
- The **arithmetic.py** file is a simple module to do arithmetic operations like addition, subtraction, multiplication and division. The **testing.py** file is another simple module which runs some testcases on the package.
- To successfully integrate **Travis CI** with your **Github** repository you will need:

  **_Step 1:_** Github repository for which you want to integrate Travis CI with
  
  **_Step 2:_** Sign In with your Github account on [https://travis-ci.org](https://travis-ci.org)
    
  **_Step 3:_** Activate the github repository from the Travis CI console for which you want to do the integration
    
  **_Step 4:_** Trigger the build by doing a ```push``` to the repository
    
  **_Step 5:_** Finally check status on Travis CI console to verify if your build passed or failed
    
### Step 1: Creating or identifying github repository
- Create a github repository like this one or identify the github repository you would like to integrate with **Travis CI**.
- :warning: Note that the this repository should be public and not private.

### Step 2: Sign In with your Github account
- Fairly straight forward, go to [https://travis-ci.org](https://travis-ci.org) and login with your Github credentials as shown below:

<p align="center"><img alt="Sign In with your github credentials" src="/misc/sign-in.png" height=90% width=90%></p>

### Step 3: Activate github repository
- After you login, navigate to the left of your console as shown below and click on the [**+**](#step-3-activate-github-repository) sign as shown below:

<p align="center"><img alt="Click the '+' sign" src="/misc/repos.png"></p>

- After clicking the **[+](#step-3-activate-github-repository)** sign you will be able to see all your public repositories

- Activate your repository for integration with Travis CI by turning on the button next to your repository as shown below:

<p align="center"><img alt="turn on the activate button" src="/misc/activate.png" height=80% width=80%></p>

### Step 4: Trigger the build
- This is the most important step of all the steps. You will need a **.travis.yml** file to trigger the **Travis CI** build.
- A **.travis.yml** or a [**_YAML_**](https://en.wikipedia.org/wiki/YAML) is a simple human readible data serialization configuration file which tells Travis CI what to do once you trigger the build. For example like the one shown below:

   ```YAML
      #declaring the type of language
      language: python
      
      #declaring the versions of the language specified above  you to want the test the code against
      python:
          - "3.5"
      
      #before executing the code installing the dependencies if any
      install:
          - pip install -r requirements.txt
      
      #running the desired code file for testing your code
      script:
          - mypy pkg/arithmetic/arithmetic.py
   ```
### Step 5: Status check
- **Travis CI** will start start the build by executing the steps as outlined in the **.travis.yml**, you can also verify this by checking the logs in the console after logging into your **Travis CI** account as shown below:

<p align="center"><img alt="see the logs" src="/misc/logs.png" height=80% width=80%></p>

- You can also verify if your build passed or failed by looking at the build batch on the top of the console as shown below:

<p align="center"><img alt="see the logs" src="/misc/batch.png" height=80% width=80%></p>
