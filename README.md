# 🌐 Professional Portfolio Website

Static portfolio website hosted on AWS S3 with global CloudFront CDN delivery. Features responsive design, dark/light theme toggle, and HTTPS encryption.

**Live Demo:** [Your CloudFront URL]

---

## 📋 Overview

Personal portfolio showcasing network engineering expertise, AWS cloud projects, and technical skills. Built with modern web technologies and deployed using Infrastructure as Code.

**Tech Stack:**
- AWS S3 (Static website hosting)
- CloudFront (Global CDN with 100+ edge locations)
- Pulumi (Infrastructure as Code)
- HTML/CSS/JavaScript (Responsive design)
- Origin Access Control (OAC) for security

**Cost:** ~$0.50/month (within AWS Free Tier for 12 months)

---

## 🏗️ Architecture

```
Users Worldwide
    ↓
CloudFront Edge Locations (HTTPS)
    ↓
Origin Access Control (OAC)
    ↓
S3 Bucket (Private)
    ├── index.html
    ├── projects.html
    ├── about.html
    ├── contact.html
    └── css/js/images
```

**Key Features:**
- ✅ Global CDN delivery (100+ edge locations)
- ✅ HTTPS/SSL encryption
- ✅ Origin Access Control for secure S3 access
- ✅ Custom error pages (404 handling)
- ✅ Gzip compression
- ✅ Cache optimization
- ✅ Dark/light theme with localStorage persistence
- ✅ Fully responsive (mobile/tablet/desktop)

---

## 🚀 Quick Start

### Prerequisites

- AWS account with credentials configured
- Pulumi CLI installed
- Python 3.8+

### Deploy Infrastructure

```bash
# Clone repository
git clone https://github.com/Sparty-5A/portfolio-website.git
cd portfolio-website

# Install dependencies
pip install -r requirements.txt

# Initialize Pulumi (local backend)
pulumi login --local
pulumi stack init dev

# Deploy to AWS
pulumi up
# Review resources and confirm: yes

# Wait 5-15 minutes for CloudFront distribution deployment
```

### Get Your Website URL

```bash
# Get CloudFront URL
pulumi stack output cloudfront_url

# Example output: https://d1234abcd.cloudfront.net
```

Your portfolio is now live! 🎉

---

## 📝 Customization

### Update Personal Information

1. **Edit HTML files in `website/` directory:**
   - `index.html` - Update name, title, bio, stats
   - `projects.html` - Add/modify projects
   - `about.html` - Update skills, certifications
   - `contact.html` - Add email, LinkedIn, GitHub

2. **Deploy changes:**
   ```bash
   pulumi up
   ```

3. **Force immediate update (optional):**
   ```bash
   # Invalidate CloudFront cache
   aws cloudfront create-invalidation \
     --distribution-id $(pulumi stack output cloudfront_distribution_id) \
     --paths "/*"
   ```

---

## 🎨 Features

### Website Pages

- **Home** - Hero section, skills overview, featured projects
- **Projects** - Detailed showcase of 6 AWS projects
- **About** - Background, skills, certifications
- **Contact** - Contact information and availability

### Design Features

- **Theme Toggle** - Dark/light mode with smooth transitions
- **Responsive** - Optimized for mobile, tablet, desktop
- **Animations** - Smooth scroll, fade-ins, hover effects
- **Performance** - Fast loading with CloudFront CDN
- **Accessibility** - Semantic HTML, ARIA labels

---

## 💰 Cost Analysis

| Service | Free Tier | Monthly Usage | Cost |
|---------|-----------|---------------|------|
| S3 Storage | 5 GB | ~10 MB | $0.00 |
| S3 Requests | 20,000 GET | ~500 | $0.00 |
| CloudFront (12 months) | 1 TB transfer | ~1 GB | $0.00 |
| CloudFront Requests | 10M/month | ~1,000 | $0.00 |
| **Total (Year 1)** | | | **$0.00** |
| **After Free Tier** | | | **~$0.50** |

---

## 📂 Project Structure

```
portfolio-website/
├── __main__.py                  # Main Pulumi deployment
├── Pulumi.yaml                  # Project configuration
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Python project metadata
│
├── infrastructure/
│   ├── __init__.py
│   ├── s3.py                    # S3 bucket configuration
│   └── cloudfront.py            # CloudFront distribution
│
├── website/                     # Website content
│   ├── index.html               # Homepage
│   ├── projects.html            # Projects showcase
│   ├── about.html               # About/skills page
│   ├── contact.html             # Contact information
│   ├── 404.html                 # Custom error page
│   │
│   ├── css/
│   │   └── style.css            # Responsive styles + themes
│   │
│   ├── js/
│   │   └── main.js              # Theme toggle, animations
│   │
│   └── images/
│       └── (your images)
│
└── README.md                    # This file
```

---

## 🔄 Update Workflow

```bash
# 1. Edit website content
nano website/index.html

# 2. Deploy changes
pulumi up

# 3. (Optional) Force immediate cache refresh
aws cloudfront create-invalidation \
  --distribution-id $(pulumi stack output cloudfront_distribution_id) \
  --paths "/*"

# Wait 1-2 minutes for invalidation to complete
```

---

## 🛠️ Development

### Local Testing

```bash
# Serve website locally for development
cd website/
python -m http.server 8000

# Open http://localhost:8000 in browser
```

### Infrastructure Validation

```bash
# Preview changes without deploying
pulumi preview

# View current stack outputs
pulumi stack output

# Check CloudFront distribution status
aws cloudfront get-distribution \
  --id $(pulumi stack output cloudfront_distribution_id)
```

---

## 🧹 Cleanup

```bash
# Destroy all AWS resources
pulumi destroy
# Confirm: yes

# Removes:
# - S3 bucket (all files deleted)
# - CloudFront distribution
# - All associated resources
```

⚠️ **Warning:** All website content will be permanently deleted!

---

## 📊 AWS Skills Demonstrated

### AWS Solutions Architect Associate Coverage

**Domain 1: Secure Architectures (30%)**
- ✅ S3 bucket policies and access control
- ✅ Origin Access Control (OAC)
- ✅ HTTPS/SSL encryption
- ✅ Blocking public S3 access

**Domain 2: Resilient Architectures (26%)**
- ✅ S3 versioning
- ✅ CloudFront global distribution
- ✅ Custom error pages

**Domain 3: High-Performing Architectures (24%)**
- ✅ CloudFront CDN for content delivery
- ✅ Edge caching
- ✅ Gzip compression

**Domain 4: Cost-Optimized Architectures (20%)**
- ✅ Serverless architecture (no EC2)
- ✅ AWS Free Tier optimization

---

## 🎓 Learning Outcomes

**Infrastructure Skills:**
- AWS S3 static website hosting
- CloudFront CDN configuration
- Origin Access Control (OAC) implementation
- Infrastructure as Code with Pulumi
- Cache invalidation strategies

**Web Development:**
- Responsive web design
- CSS custom properties (CSS variables)
- JavaScript theme toggle
- LocalStorage persistence
- Modern HTML5 semantics

---

## 🔧 Troubleshooting

### Issue: CloudFront shows "Access Denied"

**Cause:** Bucket policy not applied correctly

**Solution:**
```bash
# Redeploy infrastructure
pulumi up
```

### Issue: Website content not updating

**Cause:** CloudFront cache

**Solution:**
```bash
# Invalidate cache
aws cloudfront create-invalidation \
  --distribution-id $(pulumi stack output cloudfront_distribution_id) \
  --paths "/*"
```

### Issue: Deployment takes too long

**Normal:** CloudFront distribution deployment takes 5-15 minutes on first deploy

**Check status:**
```bash
pulumi stack output cloudfront_distribution_id
aws cloudfront get-distribution --id <distribution-id>
```

---

## 🎯 Future Enhancements

**Planned Features:**
- [ ] Custom domain with Route 53
- [ ] Contact form with Lambda + API Gateway
- [ ] Blog section with markdown support
- [ ] Analytics integration (CloudWatch)
- [ ] CI/CD pipeline with GitHub Actions
- [ ] A/B testing capabilities

---

## 📚 Resources

**AWS Documentation:**
- [S3 Static Website Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)
- [Origin Access Control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Pulumi Documentation:**
- [Pulumi AWS S3](https://www.pulumi.com/registry/packages/aws/api-docs/s3/)
- [Pulumi AWS CloudFront](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 👤 Author

**Scott Penry**
- GitHub: [@Sparty-5A](https://github.com/Sparty-5A)
- LinkedIn: [scott-penry-0a277829](https://linkedin.com/in/scott-penry-0a277829)
- Website: [Your CloudFront URL]

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you learn AWS S3 and CloudFront!

---

**Built with AWS, Pulumi, and modern web technologies** ☁️