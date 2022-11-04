pipeline {
    agent any 
    stages {
        stage('clone stocksDB') {
            when {
                expression { return params.current_status == "closed" && params.merged == true }
            }
            steps {
                echo 'cloning stocksDB'
                sh 'rm -fr stocksDB'
                sh 'git clone https://github.com/Albert-Lepree/stocksDB.git'
            }
        }
        stage('Update stocksDB') {
             when {
                expression { return params.current_status == "closed" && params.merged == true }
            }
            steps {
                echo 'updating /app/seed/stocksDB'
                sh 'ssh -i /home/jenkins/.ssh/finniscool.pem ubuntu@ec2-18-234-190-54.compute-1.amazonaws.com sudo git -C /home/ubuntu/updater/stocksDB pull https://github.com/Albert-Lepree/stocksDB.git master'
            }
        }
    }
    }
