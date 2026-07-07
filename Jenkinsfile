pipeline {

    agent any

    stages {

        stage('Hello') {
            steps {
                echo 'Hello from Jenkins!'
            }
        }


        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Requirements') {
            steps {
                 sh 'pip3 install --break-system-packages -r requirements.txt'
             }
        }
        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }


        stage('List Files') {
            steps {
                sh 'ls -la'
            }
        }


        stage('Docker Build Image') {
            steps {
                sh 'docker build -t prithvia24/flask-app:${BUILD_NUMBER} .'
            }
        }


        stage('Docker Push') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                    echo $DOCKER_PASS | docker login \
                    -u $DOCKER_USER \
                    --password-stdin

                    docker push prithvia24/flask-app:${BUILD_NUMBER}
                    '''
                }
         stage('Deploy') {
            steps {
                sh '''
                docker stop flask-container || true
                docker rm flask-container || true

                docker run -d \
                --name flask-container \
                -p 5000:5000 \
                prithvia24/flask-app:${BUILD_NUMBER}
                '''
            }
        }
            }
        }

    }
}