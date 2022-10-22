git config --global user.name "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add -A && git commit -m "$PACKAGE_NAME NEW VERSION"
git push origin HEAD:main
