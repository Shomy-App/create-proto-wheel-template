git config --global user.name ${GITHUB_ACTOR}
git config --global user.email ${GITHUB_ACTOR}@users.noreply.github.com
git add -A && git commit -m "$PACKAGE_NAME NEW VERSION"
git push -u origin main
