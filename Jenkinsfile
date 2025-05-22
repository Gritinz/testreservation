pipeline {
    agent any
    environment {
        BRANCH_NAME = powershell(script: "git rev-parse --abbrev-ref HEAD", returnStdout: true).trim()
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Dev') {
            when {
                anyOf {
                    branch 'develop'
                    branch 'feature/*'
                }
            }
            steps {
                dir('.') {
                    bat 'docker-compose -f docker-compose.prod.yml build'
                }
            }
        }

        stage('Run Dev') {
            when {
                anyOf {
                    branch 'develop'
                    branch 'feature/*'
                }
            }
            steps {
                dir('.') {
                    bat 'docker-compose -f docker-compose.prod.yml up -d'
                }
            }
        }

        stage('Build Prod') {
            when {
                branch 'main'
            }
            steps {
                dir('.') {
                    bat 'docker-compose -f docker-compose.prod.yml build'
                }
            }
        }

        stage('Deploy Prod') {
            when {
                branch 'main'
            }
            steps {
                dir('.') {
                    bat 'docker-compose -f docker-compose.prod.yml up -d'
                }
            }
        }
    }
}