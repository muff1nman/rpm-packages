node('docker && fedora26') {
    stage 'Source Checkout'
    scm checkout

    stage 'Full Repo release'
    sh "./build-repo ${repoName}"
}
