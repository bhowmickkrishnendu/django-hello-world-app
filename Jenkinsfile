// This script is Writen by Krishnendu Bhowmick
node{
    
    def buildnumber = BUILD_NUMBER
    
    stage("Project Clone")
    {
        checkout scmGit(
        branches: [[name: 'master']],
        userRemoteConfigs: [[url: 'https://github.com/bhowmickkrishnendu/django-hello-world-app.git']])
    }
    //SSH Credentials plugin used.
    stage('Docker Image Build')
    {
        sshagent(['Docker_Server_Login']) 
        {
            sh "ssh -o StrictHostKeyChecking=no ubuntu@172.31.34.143 docker image prune -f --all"
            //sh "pwd"
            //sh "ls -la"
            sh "scp -o StrictHostKeyChecking=no -r * ubuntu@172.31.34.143:/home/ubuntu/django-hello-world-app/"
            sh "ssh -o StrictHostKeyChecking=no ubuntu@172.31.34.143 'cd django-hello-world-app && docker build -t krishhub/django-hello-app:${buildnumber} .'"
            sh "ssh -o StrictHostKeyChecking=no ubuntu@172.31.34.143 docker push krishhub/django-hello-app:${buildnumber}"
        }
    }
    
    //SSH Credentials plugin used.
    stage('Docker Image Push')
    {
        sshagent(['Docker_Server_Login']) 
        {
            sh "ssh -o StrictHostKeyChecking=no ubuntu@172.31.34.143 docker push krishhub/django-hello-app:${buildnumber}"
        }
    }
    
    //SSH Credentials plugin used.
    stage('Update Build Tag on K8s Deployment YML')
    {
        
    sh "chmod +x changebuildtag.sh"
    sh "./changebuildtag.sh ${buildnumber}"
    
    }
    
    //SSH Credentials plugin used.
    stage('Deploy Python app on k8s')
    {
        sshagent(['K8s_Server_Login']) {
            
            sh "ssh -o StrictHostKeyChecking=no ubuntu@172.31.34.86"
            sh "scp -o StrictHostKeyChecking=no deploy-pythonapp.yml ubuntu@172.31.34.86:/home/ubuntu/"
            sh "ssh ubuntu@172.31.34.86 kubectl apply -f deploy-pythonapp.yml"
            
        }
    }
}
