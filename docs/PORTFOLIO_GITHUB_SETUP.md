# 🚀 GitHub Setup Guide - Portfolio Website

Complete guide to publishing your portfolio website to GitHub.

---

## 📋 **Pre-Publishing Checklist**

### **1. Update Website Content**

```bash
cd ~/AWS_cloud/aws_s3_cloudfront/website/

# Replace ALL placeholder content:
```

**Files to Update:**
- ✅ `index.html` - Your name, title, bio
- ✅ `about.html` - Your background, skills
- ✅ `contact.html` - Your email, LinkedIn, GitHub
- ✅ `projects.html` - Your actual projects (already has 6!)

**Search and Replace:**
```bash
# Example replacements (do manually or with sed):
"Your Name" → "Scott Penry"
"your.email@example.com" → "scottpenry@comcast.net"
"yourlinkedin" → "scott-penry-0a277829"
"yourgithub" → "Sparty-5A"
```

### **2. Copy GitHub Files**

```bash
cd ~/AWS_cloud/aws_s3_cloudfront/

# Copy all the files I created:
cp /path/to/portfolio-README.md README.md
cp /path/to/portfolio-gitignore .gitignore
cp /path/to/portfolio-pyproject.toml pyproject.toml
cp /path/to/portfolio-requirements.txt requirements.txt
cp /path/to/portfolio-Pulumi.yaml Pulumi.yaml
```

### **3. Clean Up**

```bash
# Remove any Pulumi stack files (they contain secrets!)
rm -f Pulumi.*.yaml

# Remove any local testing files
rm -rf __pycache__
rm -rf .pulumi/
rm -rf venv/
rm -rf .venv/

# Keep ONLY these Pulumi-related files:
# ✅ Pulumi.yaml (base config - safe to commit)
# ❌ Pulumi.dev.yaml, Pulumi.*.yaml (contain secrets - don't commit!)
```

---

## 🎯 **GitHub Repository Setup**

### **Step 1: Initialize Git**

```bash
cd ~/AWS_cloud/aws_s3_cloudfront/

# Initialize git repository
git init

# Add all files
git add .

# Check what will be committed
git status

# Should NOT see:
# ❌ Pulumi.*.yaml (stack configs)
# ❌ __pycache__/
# ❌ venv/ or .venv/
# ❌ .pulumi/

# Should see:
# ✅ README.md
# ✅ Pulumi.yaml
# ✅ __main__.py
# ✅ infrastructure/
# ✅ website/
# ✅ requirements.txt
# ✅ pyproject.toml
```

### **Step 2: Commit**

```bash
# Make initial commit
git commit -m "Initial commit: Portfolio website with S3 and CloudFront

- Static website hosted on AWS S3
- Global CDN delivery via CloudFront
- Origin Access Control (OAC) for security
- Responsive design with dark/light theme
- Infrastructure as Code with Pulumi
- 4 page portfolio (home, projects, about, contact)
- HTTPS encryption and custom error pages"
```

### **Step 3: Create GitHub Repository**

**Using GitHub CLI (recommended):**
```bash
# Create public repository and push
gh repo create portfolio-website \
  --public \
  --description "Professional portfolio website hosted on AWS S3 with CloudFront CDN" \
  --push \
  --source .
```

**Or manually:**
1. Go to https://github.com/new
2. Repository name: `portfolio-website`
3. Description: "Professional portfolio website hosted on AWS S3 with CloudFront CDN"
4. Visibility: **Public**
5. **Do NOT** initialize with README (you already have one)
6. Click **Create repository**

Then push:
```bash
git remote add origin https://github.com/Sparty-5A/portfolio-website.git
git branch -M main
git push -u origin main
```

---

## 🏷️ **Add GitHub Topics**

### **Recommended Topics (10 total):**

```bash
# Using GitHub CLI
gh repo edit --add-topic aws,s3,cloudfront,pulumi,portfolio,infrastructure-as-code,static-website,python,cdn,web-development
```

**Or add manually in GitHub UI:**
- `aws`
- `s3`
- `cloudfront`
- `pulumi`
- `portfolio`
- `infrastructure-as-code`
- `static-website`
- `python`
- `cdn`
- `web-development`

---

## 📌 **Pin to Profile**

```bash
# Pin repository (GitHub UI)
# 1. Go to your profile: https://github.com/Sparty-5A
# 2. Click "Customize your pins"
# 3. Select "portfolio-website"
# 4. Click "Save pins"
```

---

## 📝 **Update Repository Settings**

### **In GitHub Repository Settings:**

1. **About Section** (top right):
   - Website: Add your CloudFront URL
   - Description: "Professional portfolio website hosted on AWS S3 with CloudFront CDN"
   - Topics: (already added above)

2. **Optional: Add Homepage URL**
   ```bash
   gh repo edit --homepage "https://your-cloudfront-url.cloudfront.net"
   ```

---

## 💼 **LinkedIn Post Template**

```
🚀 New Project: Professional Portfolio Website with AWS S3 + CloudFront

Just deployed my portfolio using AWS cloud infrastructure:

🌐 Global CDN delivery via CloudFront (100+ edge locations)
🔒 Origin Access Control (OAC) for secure S3 access
⚡ HTTPS encryption with CloudFront default certificate
🎨 Responsive design with dark/light theme toggle
📦 Infrastructure as Code using Pulumi

This project demonstrates:
✅ AWS S3 static website hosting
✅ CloudFront distribution configuration
✅ Security best practices (OAC, encryption)
✅ Cost optimization (~$0.50/month)
✅ Modern web development (HTML/CSS/JS)

Key technical implementations:
• Origin Access Control instead of legacy OAI
• Custom error responses for SPA-style routing
• Gzip compression and cache optimization
• Pulumi IaC for reproducible deployments

💰 Cost-conscious: Runs on AWS Free Tier (year 1), then ~$0.50/month

Check it out: https://github.com/Sparty-5A/portfolio-website

#AWS #CloudFront #S3 #Pulumi #InfrastructureAsCode #WebDevelopment #Portfolio
```

---

## 🎯 **Resume Bullet Points**

### **Option 1 (Infrastructure Focus):**
```
Portfolio Website - AWS S3 + CloudFront                    Dec 2024
AWS S3, CloudFront, OAC, Pulumi, HTML/CSS/JS

• Deployed static website on AWS S3 with global CDN delivery via
  CloudFront, serving content from 100+ edge locations worldwide

• Implemented Origin Access Control (OAC) for secure S3 bucket access,
  preventing direct public access while enabling CloudFront distribution

• Built responsive portfolio with dark/light theme toggle using vanilla
  JavaScript, demonstrating frontend development capabilities

• Achieved ~$0.50/month operational cost through AWS Free Tier
  optimization while maintaining production-ready infrastructure

• Deployed infrastructure using Pulumi IaC, enabling reproducible and
  version-controlled infrastructure management
```

### **Option 2 (Skills Breadth):**
```
Full-Stack Portfolio Website with AWS Infrastructure       Dec 2024

• Architected and deployed production-grade static website using AWS S3
  with CloudFront CDN, implementing security best practices including
  Origin Access Control and HTTPS encryption

• Developed responsive web interface with dark/light theme toggle,
  smooth animations, and mobile-first design approach

• Automated infrastructure deployment using Pulumi IaC with Python,
  ensuring reproducible and version-controlled infrastructure

• Optimized for cost (~$0.50/month) and performance (global CDN with
  edge caching and compression)
```

---

## 📊 **Project Statistics**

Add these to your README or LinkedIn post:

```
Project Metrics:
• Lines of Code: ~500 (Python IaC) + ~2,500 (HTML/CSS/JS)
• Infrastructure: 5 AWS resources (S3, CloudFront, OAC, policies)
• Pages: 4 (Home, Projects, About, Contact)
• Features: Theme toggle, responsive design, smooth animations
• Cost: $0.00/month (Free Tier), then ~$0.50/month
• Deployment Time: ~15 minutes (5 min code, 10 min CloudFront)
• Global Reach: 100+ CloudFront edge locations
```

---

## ✅ **Final Checklist**

Before marking as complete:

- [ ] Updated all website content with your information
- [ ] Removed all placeholder text
- [ ] Copied all GitHub files (README, .gitignore, etc.)
- [ ] Cleaned up Pulumi stack files
- [ ] Initialized git repository
- [ ] Made initial commit
- [ ] Created GitHub repository (public)
- [ ] Pushed code to GitHub
- [ ] Added topics to repository
- [ ] Pinned repository to profile
- [ ] Updated repository About section
- [ ] Added CloudFront URL to repo (once deployed)
- [ ] Posted on LinkedIn
- [ ] Updated resume with project

---

## 🎉 **Post-Publishing**

### **Share Your Work:**

1. **LinkedIn Post** - Use template above
2. **Twitter/X** - Share your CloudFront URL
3. **Resume** - Add project with bullet points
4. **GitHub Profile README** - Link to portfolio

### **Monitor Performance:**

```bash
# Check CloudFront metrics
aws cloudfront get-distribution-statistics \
  --distribution-id $(pulumi stack output cloudfront_distribution_id)

# View S3 bucket size
aws s3 ls s3://$(pulumi stack output bucket_name) --summarize --human-readable --recursive
```

---

## 🔄 **Future Updates Workflow**

```bash
# 1. Edit website files
nano website/index.html

# 2. Commit changes
git add website/
git commit -m "Update: Added new project to portfolio"

# 3. Push to GitHub
git push

# 4. Deploy to AWS
pulumi up

# 5. Invalidate cache (if needed)
aws cloudfront create-invalidation \
  --distribution-id $(pulumi stack output cloudfront_distribution_id) \
  --paths "/*"
```

---

## 💡 **Pro Tips**

1. **Always test locally** before deploying to AWS
2. **Use meaningful commit messages** for better project history
3. **Keep CloudFront URL** in repository About section
4. **Update LinkedIn** when you add new features
5. **Monitor AWS costs** (should stay under $1/month)

---

## 🎯 **Success Metrics**

Your portfolio website is successful when:

- ✅ Loads in under 2 seconds globally
- ✅ Responsive on all device sizes
- ✅ Theme toggle works smoothly
- ✅ Costs under $1/month
- ✅ Gets noticed by recruiters
- ✅ Showcases your technical skills effectively

---

**Ready to publish? Follow the steps above and make your portfolio live!** 🚀

**Your portfolio website will be your 6th public project!** 🎉
