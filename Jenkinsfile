pipeline {
    agent any 
    stages {
        stage('clone stocksDB') {
            steps {
                echo 'cloning stocksDB'
                sh 'rm -fr stocksDB'
                sh 'git clone https://github.com/Albert-Lepree/stocksDB.git'
            }
        }
        stage('Update stocksDB') {
            steps {
                echo 'updating /app/seed/stocksDB'
                sh 'whoami'
                sh 'git -C /app/seed/stocksDB pull'
            }
        }
    }
    }
