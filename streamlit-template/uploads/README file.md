# Streamlit-based Web Application
####INSIGHTHUB ANALYTICS

## 1) Overview

![Streamlit](resources/imgs/streamlit.png)

Welcome to the README file for managing Fiber Lease Agreements under International Financial Reporting Standard 16 (IFRS 16). This document provides a brief overview of how IFRS 16, developed by the International Accounting Standards Board (IASB), applies to the accounting treatment of fiber lease agreements in your financial statements.


#### 1.1) What is IFRS 16?

IFRS 16 is a comprehensive set of accounting standards designed by the IASB to guide companies in accounting for leases in their financial statements. It ensures a consistent and transparent approach to lease accounting across various industries.
##### Description of files

For this repository, we are only concerned with a single file:

| File Name              | Description                       |
| :--------------------- | :--------------------             |
| `base_app.py`          | Streamlit application definition. |

## 2) Usage Instructions

#### 2.1) Creating a copy of this repo

| :zap: WARNING :zap:                                                                                     |
| :--------------------                                                                                   |
| Do **NOT** *clone* this repository. Instead follow the instructions in this section to *fork* the repo. |

As described within the Predict instructions for the Classification Sprint, this code represents a *template* from which to extend your own work. As such, in order to modify the template, you will need to **[fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)** this repository. Failing to do this will lead to complications when trying to work on the web application remotely.

![Fork Repo](resources/imgs/fork-repo.png)  

To fork the repo, simply ensure that you are logged into your GitHub account, and then click on the 'fork' button at the top of this page as indicated within the figure above.

#### 2.2) Running the Streamlit web app on your local machine

As a first step to becoming familiar with our web app's functioning, we recommend setting up a running instance on your own local machine.

To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

 1. Ensure that you have the prerequisite Python libraries installed on your local machine:

 ```bash
 pip install -U streamlit numpy pandas scikit-learn
 ```

 2. Clone the *forked* repo to your local machine.

 ```bash
 git clone https://github.com/{your-account-name}/classification-predict-streamlit-template.git
 ```  

 3. Navigate to the base of the cloned repo, and start the Streamlit app.

 ```bash
 cd classification-predict-streamlit-template/
 streamlit run base_app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```

You should also be automatically directed to the base page of your web app. This should look something like:

![Streamlit base page](resources/imgs/streamlit-base-splash-screen.png)

Congratulations! You've now officially deployed your first web application!

While we leave the modification of your web app up to you, the latter process of cloud deployment is outlined within the next section.  

#### 2.4) Running Streamlit on a remote AWS EC2 instance


The following steps will enable you to run your web app on a remote EC2 instance, allowing it to the accessed by any device/application which has internet access.

Within these setup steps, we will be using a remote EC2 instance, which we will refer to as the ***Host***, in addition to our local machine, which we will call the ***Client***. We use these designations for convenience, and to align our terminology with that of common web server practices. In cases where commands are provided, use Git bash (Windows) or Terminal (Mac/Linux) to enter these.

1. Ensure that you have access to a running AWS EC2 instance with an assigned public IP address.

**[On the Host]:**

2. Install the prerequisite python libraries:

```bash
pip install -U streamlit numpy pandas scikit-learn
```

3. Clone your copy of the API repo, and navigate to its root directory:

```bash
git clone https://github.com/{your-account-name}/classification-predict-streamlit-template.git
cd classification-predict-streamlit-template/
```

| :information_source: NOTE :information_source:                                                                                                    |
| :--------------------                                                                                                                             |
| In the following steps we make use of the `tmux` command. This programme has many powerful functions, but for our purposes, we use it to gracefully keep our web app running in the background - even when we end our `ssh` session. |

4. Enter into a Tmux window within the current directory. To do this, simply type `tmux`.  

5. Start the Streamlit web app on port `5000` of the host

```bash
streamlit run --server.port 5000 base_app.py
```

If this command ran successfully, output similar to the following should be observed on the Host:

```
You can now view your Streamlit app in your browser.

  Network URL: http://172.31.47.109:5000
  External URL: http://3.250.50.104:5000

```

Where the specific `Network` and `External` URLs correspond to those assigned to your own EC2 instance. Copy the value of the external URL.  

**[On the Client]:**

6.  Within your favourite web browser (we hope this isn't Internet Explorer 9), navigate to external URL you just copied from the Host. This should correspond to the following form:

    `http://{public-ip-address-of-remote-machine}:5000`   

    Where the above public IP address corresponds to the one given to your AWS EC2 instance.

    If successful, you should see the landing page of your streamlit web app:

![Streamlit base page](resources/imgs/streamlit-base-splash-screen.png)

**[On the Host]:**

7. To keep your web app running continuously in the background, detach from the Tmux window by pressing `ctrl + b` and then `d`. This should return you to the view of your terminal before you opened the Tmux window.

    To go back to your Tmux window at any time (even if you've left your `ssh` session and then return), simply type `tmux attach-session`.

    To see more functionality of the Tmux command, type `man tmux`.

Having run your web app within Tmux, you should be now free to end your ssh session while your webserver carries on purring along. Well done :zap:!
## 3) About us
Welcome to our dynamic team, where a fusion of diverse skills and a shared passion for unlocking the power within data defines us. Comprising dedicated data scientists, analysts, and innovators, we are united by a common goal: unraveling the vast potential concealed within information. Our approach seamlessly blends advanced analytics with industry expertise, allowing us to navigate the complexities of data and extract meaningful insights. Join us on a journey where collective knowledge transforms into actionable solutions, driving innovation and making a lasting impact in the world of data exploration.
### 3.1) Meet our lovely team
* Boitumelo Mphahlele  
* Koketso Napo  
* Nomfundo Ncube 

## 4) FAQ

This section of the repo will be periodically updated to represent common questions which may arise around its use. If you detect any problems/bugs, please [create an issue](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue) and we will do our best to resolve it as quickly as possible.

We wish you all the best in your learning experience :rocket:

![Explore Data Science Academy](resources/imgs/EDSA_logo.png)
