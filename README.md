# RiskInDroid CLI
### This Cli implimentation of original [RisdInDroid](https://github.com/ClaudiuGeorgiu/RiskInDroid)
> A tool for quantitative risk analysis of Android applications based on machine
> learning techniques.

[![Codacy](https://app.codacy.com/project/badge/Grade/13be50b318c74ac88fba3e13bd620f9c)](https://www.codacy.com/gh/ClaudiuGeorgiu/RiskInDroid)
[![Actions Status](https://github.com/ClaudiuGeorgiu/RiskInDroid/workflows/Build/badge.svg)](https://github.com/ClaudiuGeorgiu/RiskInDroid/actions?query=workflow%3ABuild)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-green.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ClaudiuGeorgiu/RiskInDroid/blob/master/LICENSE)



**RiskInDroid** (**Ri**sk **In**dex for An**droid**) is a tool for quantitative risk
analysis of Android applications written in Java (used to check the permissions of the
apps) and Python (used to compute a risk value based on apps' permissions). The tool
uses classification techniques through *scikit-learn*, a machine learning library for
Python, in order to generate a numeric risk value between 0 and 100 for a given app.
In particular, the following classifiers of *scikit-learn* are used in **RiskInDroid**
(this list is chosen after extensive empirical assessments):
* Support Vector Machines (SVM)
* Multinomial Naive Bayes (MNB)
* Gradient Boosting (GB)
* Logistic Regression (LR)

Unlike other tools, **RiskInDroid** does not take into consideration only the
permissions declared into the app manifest, but carries out reverse engineering on
the apps to retrieve the bytecode and then infers (through static analysis) which
permissions are actually used and which not, extracting in this way 4 sets of
permissions for every analyzed app:
* Declared permissions - extracted from the app manifest
* Exploited permissions - declared and actually used in the bytecode
* Ghost permissions - not declared but with usages in the bytecode
* Useless permissions - declared but never used in the bytecode

From the above sets of permissions (and considering only the official list of Android
permissions), feature vectors (made by `0`s and `1`s) are built and given to the
classifiers, which then compute a risk value. The precision and the reliability of
**RiskInDroid** have been empirically tested on a dataset made of more than 6K malware
samples and 112K apps.

`NOTE:` the data collection and the experiments took place in late 2016. Since then, the
used libraries have been updated and the models have been retrained (by using the same
dataset), so the current results might slightly differ from the original.



## ❱ Publication

More details about **RiskInDroid** can be found in the paper
"[RiskInDroid: Machine Learning-based Risk Analysis on Android](https://github.com/ClaudiuGeorgiu/RiskInDroid/blob/master/docs/paper/RiskInDroid.pdf)"
([official publication link](https://link.springer.com/chapter/10.1007/978-3-319-58469-0_36)).
You can cite the paper as follows:

> A. Merlo, G.C. Georgiu. "RiskInDroid: Machine Learning-based Risk Analysis on Android",
> in *Proceedings of the 32nd International Conference on ICT Systems Security and
> Privacy Protection* ([IFIP-SEC 2017](http://www.ifipsec.org/)).

```BibTeX
@Inbook{RiskInDroid,
  author="Merlo, Alessio and Georgiu, Gabriel Claudiu",
  editor="De Capitani di Vimercati, Sabrina and Martinelli, Fabio",
  title="RiskInDroid: Machine Learning-Based Risk Analysis on Android",
  bookTitle="ICT Systems Security and Privacy Protection: 32nd IFIP TC 11 International Conference, SEC 2017, Rome, Italy, May 29-31, 2017, Proceedings",
  year="2017",
  publisher="Springer International Publishing",
  pages="538--552",
  isbn="978-3-319-58469-0",
  doi="10.1007/978-3-319-58469-0_36",
  url="https://doi.org/10.1007/978-3-319-58469-0_36"
}
```



## ❱ Demo



## ❱ Installation & Usage

```sh
# Clone the repo
git clone https://github.com/anurag3301/RiskInDroid.git

# cd into the RiskInDroid folder
cd RiskInDroid

# Install the dependecies
pip install -r requirements.txt

# See The usage
python3 app/main.py --help

# Do a test run, print the result on terminal
python3 app/main.py --cli --file ./app/test/test_resources/InsecureBankv2.apk

# Do a test run, print the result on terminal and store the result in json file
python3 app/main.py --cli --out ./ --file ./app/test/test_resources/InsecureBankv2.apk
# This will create a new directory name results, the results will be stored there

# Do a test on directory containing lot of apks 
# print the result on terminal and store the result in json file
python3 app/main.py --cli --out ./ --dir ./app/test/test_resources
```



## ❱ Contributing

Questions, bug reports and pull requests are welcome on GitHub at
[https://github.com/ClaudiuGeorgiu/RiskInDroid](https://github.com/ClaudiuGeorgiu/RiskInDroid).



## ❱ License

With the exception of
[PermissionChecker.jar](https://github.com/ClaudiuGeorgiu/RiskInDroid/blob/master/app/PermissionChecker.jar),
you are free to use this code under the
[MIT License](https://github.com/ClaudiuGeorgiu/RiskInDroid/blob/master/LICENSE).

[PermissionChecker.jar](https://github.com/ClaudiuGeorgiu/RiskInDroid/blob/master/app/PermissionChecker.jar)
belongs to [Talos srls](http://www.talos-sec.com/) and you can use it "AS IS" with
RiskInDroid, for research purposes only.
