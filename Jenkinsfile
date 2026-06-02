pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'flask-cicd-app'
        DOCKER_TAG = 'latest'
        CONTAINER_NAME = 'flask-app-container'
        APP_PORT = '5000'
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
                echo 'Build completed successfully!'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    bat "docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} pytest test_app.py -v"
                }
                echo 'Tests passed successfully!'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                script {
                    // إيقاف وحذف الحاوية القديمة بأمان على الويندوز
                    bat "docker stop ${CONTAINER_NAME} || set errorlevel=0"
                    bat "docker rm ${CONTAINER_NAME} || set errorlevel=0"
                    
                    // تشغيل الحاوية الجديدة
                    bat "docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
                echo 'Deployment completed successfully!'
                echo "Application is running at http://localhost:${APP_PORT}"
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline executed successfully!'
            echo "Application URL: http://localhost:${APP_PORT}"
        }
        failure {
            echo '❌ Pipeline failed!'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}