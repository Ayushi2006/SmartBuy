# Contributing Guide

Thank you for your interest in contributing! This guide will walk you through the complete workflow for contributing to this project using Git and GitHub.

---

## 📌 Prerequisites

Make sure you have:

* Git installed
* A GitHub account
* Basic knowledge of Git commands

---

## 🔁 Contribution Workflow Overview

1. Fork the repository
2. Clone your fork
3. Add upstream remote
4. Create a feature branch
5. Make changes
6. Commit and push to your fork
7. Sync with upstream
8. Open a Pull Request (PR)

---

## 🍴 1. Fork the Repository

* Go to the original repository on GitHub
* Click the **Fork** button (top-right)
* This creates a copy in your GitHub account

---

## 💻 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

---

## 🔗 3. Add Upstream Remote

This lets you keep your fork updated with the original repo.

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/REPO_NAME.git
```

Verify remotes:

```bash
git remote -v
```

---

## 🌿 4. Create a Feature Branch

Always create a new branch for each feature or fix:

```bash
git checkout -b feature/your-feature-name
```

Branch naming examples:

* feature/add-login
* fix/navbar-bug
* docs/update-readme

---

## ✍️ 5. Make Changes

* Write clean, readable code
* Follow project coding standards
* Add tests if required
* Update documentation if needed

---

## 💾 6. Commit Changes

Stage and commit your changes:

```bash
git add .
git commit -m "feat: add login functionality"
```

Commit message guidelines:

* Use present tense
* Be descriptive
* Follow conventional commits if applicable

---

## 🚀 7. Push to Your Fork (Origin)

```bash
git push origin feature/your-feature-name
```

---

## 🔄 8. Sync with Upstream

Before opening a PR, ensure your branch is up to date.

```bash
git checkout main
git pull upstream main
```

Then rebase your feature branch:

```bash
git checkout feature/your-feature-name
git rebase main
```

Resolve conflicts if any, then continue:

```bash
git rebase --continue
```

Push updated branch:

```bash
git push origin feature/your-feature-name --force
```

---

## 🔀 9. Create a Pull Request (PR)

* Go to your fork on GitHub
* Click **Compare & pull request**
* Base repo: original repository
* Base branch: main
* Head repo: your fork
* Compare branch: feature branch

### PR Guidelines:

* Clearly describe what you did
* Link related issues (e.g., "Fixes #123")
* Add screenshots if UI changes
* Keep PRs small and focused

---

## 🔁 10. Update Your Fork's Main Branch

After your PR is merged:

```bash
git checkout main
git pull upstream main
git push origin main
```

---

## 🔄 11. Create PR from Fork Main to Upstream (Advanced)

If you made changes directly to your fork's main (not recommended):

* Push your main branch:

```bash
git push origin main
```

* Open PR from your fork's main → upstream main

---

## ⚠️ Best Practices

* Never commit directly to main
* Always use feature branches
* Pull before pushing
* Keep commits atomic and meaningful
* Write clear PR descriptions
* Respect project guidelines and maintainers

---

## 🧪 Testing

* Run tests before submitting PR
* Ensure no build errors
* Follow test coverage requirements

---

## 📚 Documentation

* Update docs for new features
* Keep README accurate
* Add inline comments where needed

---

## 🐛 Reporting Issues

When creating an issue:

* Use a clear title
* Describe expected vs actual behavior
* Include steps to reproduce
* Add screenshots/logs if applicable

---

## 🤝 Code of Conduct

* Be respectful and inclusive
* Provide constructive feedback
* Collaborate openly

---

## ❓ Need Help?

* Check existing issues
* Ask questions in discussions
* Reach out to maintainers

---

Happy Contributing! 🚀
