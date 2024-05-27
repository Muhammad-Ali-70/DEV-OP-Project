pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Application build stage...' 
        }
       }
        stage('Test') {
            steps {
        sh '''
         gcloud compute scp /var/lib/jenkins/workspace/Dev-Op-Project_main/index.html root@ali-devops-project-server:/var/www/html --zone=us-central1-a
        '''
      }
        }
        stage('Run') {
            steps {
                echo 'Application run stage' 
            }
        }
    }
}
