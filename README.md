# creditworthiness_api
An API that helps companies predict if the user meets up to the criteria for getting a Loan.


![image](https://user-images.githubusercontent.com/92530942/212409021-5d9e5753-f2b2-48fb-a15e-aecab6240e8a.png)
[Image Source](https://www.iedunote.com/creditworthiness)

## Credit Worthiness Model and API

### Introduction
The Creditworthiness project is a solution for financial institutions to predict the likelihood of default for a loan applicant. The project includes a credit worthiness model, which is a machine learning model trained on historical data, and a web-based API that provides access to the model. The API allows financial institutions to easily integrate the model into their lending workflow and make informed lending decisions.

### Model
The creditworthiness model is a machine learning model that is trained to predict the likelihood of default for a loan applicant. The model is trained on a dataset that contains information about the loan applicant such as their age, income, home ownership status, employment length, loan intent, loan grade, loan amount, interest rate, percent of income represented by the loan, credit history length, and historical default status. The model is trained using a logistic regression algorithm. The model is trained on the training data set and then tested on the testing data set to evaluate its performance.

### API
The CreditWorthiness API is a web-based API that provides access to the credit worthiness model. It is built using *`FastAPI`*, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. The API is designed to work with real-time data, making it easy to integrate with existing systems. The API has been containerized using *`Docker`*, allowing it to be easily deployed and run in any environment.

### Features For Input
The model uses the following features as input:


| **Features**  | **Description** |
| ------------- | ------------- |
| `person_age` | The age of the customer |
| `person_income` | The annual income of the customer |
| `person_home_ownership` | The home ownership status of the customer (e.g. "rent", "own", "mortgage") |
| `person_emp_length` | The length of the customer's employment (in years) |
| `loan_intent` | The intent of the loan |
| `loan_grade` | The grade assigned to the loan (e.g. "A", "B", "C") |
| `loan_amnt` | The amount of the loan |
| `loan_int_rate` | The interest rate of the loan |
| `loan_percent_income` | The percent of income the loan represents |
| `cb_person_default_on_file` | Historical default of the customer (0 = no default, 1 = default) |
| `cb_preson_cred_hist_length` | Credit history length of the customer |

### Output
The model generates a binary output, where a `0 represents a non-default` and a `1 represents a default`. The API returns the output in the form of a JSON object with a single key-value pair, where the key is "prediction" and the value is the binary output. 

### Deployment
- The API is deployed using FastAPI. The model is loaded during the startup of the application using the joblib library and the load_model() method. The predict method takes in the input data in the form of a JSON object, and returns the prediction as a JSON response.
-  The API has been containerized using Docker, allowing it to be easily deployed and run in any environment.

### How to use
You can use the API by sending a POST request to the /predict endpoint with the appropriate input features in the request body. The API will return a binary output indicating the likelihood of default.


### Support
Please open an issue on the GitHub repository if you have any questions or issues with the API.

### Conclusion
- The Credit Worthiness project provides financial institutions with a solution to predict the likelihood of default for a loan applicant. The project includes a credit worthiness model and a web-based API that makes it easy to integrate the model into the lending workflow. However, it's important to use it in conjunction with other tools and factors in the lending decision process. It is important to note that this model is trained on historical data and may not always accurately predict default risk for all customers. 
- Other factors such as changes in the economy or a customer's personal circumstances may also affect their ability to repay a loan. This model should be used as one tool among many in the lending decision process.


