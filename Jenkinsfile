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
                sh 'ssh -i /.ssh/finniscool.pem ubuntu@ec2-18-234-190-54.compute-1.amazonaws.com sudo git -C /app/seed/stocksDB pull'
            }
        }
    }
    }
