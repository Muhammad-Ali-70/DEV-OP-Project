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
         gcloud compute scp --recurse /var/lib/jenkins/workspace/Dev-Op-Project_main/ root@ali-devops-project-server:/var/www/html --zone=us-central1-a
         gcloud compute ssh root@ali-devops-project-server --zone=us-central1-a -- "rm -rf /var/www/html/*"
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
