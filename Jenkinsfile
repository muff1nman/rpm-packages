node('docker && fedora26') {
    stage 'Source Checkout'
    checkout scm

    stage 'Full Repo release'
    sh "./build-repo ${repoName}"
}
