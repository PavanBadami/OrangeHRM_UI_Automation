pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_MARKER',
            choices: ['all', 'smoke', 'sanity', 'regression'],
            description: 'Select test suite to execute'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/PavanBadami/OrangeHRM_UI_Automation.git'
            }
        }

        stage('Verify Environment') {
            steps {
                bat 'python --version'
                bat 'pip --version'
                bat 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {

                    if (params.TEST_MARKER == 'all') {
                        bat 'pytest --alluredir=allure-results'
                    } else {
                        bat "pytest -m ${params.TEST_MARKER} --alluredir=allure-results"
                    }

                }
            }
        }
    }

    post {
        always {
            allure(
                includeProperties: false,
                results: [[path: 'allure-results']]
            )
        }
    }
}