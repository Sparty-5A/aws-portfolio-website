"""
Professional Portfolio Website with S3 and CloudFront
Global CDN delivery with HTTPS
"""
import pulumi
from infrastructure.s3 import create_s3_bucket, create_bucket_policy, upload_website_files
from infrastructure.cloudfront import create_cloudfront_distribution

# Project configuration
project_name = "portfolio"

print("🚀 Deploying Professional Portfolio Website...")
print(f"📍 Project: {project_name}")
print("")

# Step 1: Create S3 bucket
print("📦 Creating S3 bucket...")
s3_config = create_s3_bucket(project_name)
bucket = s3_config["bucket"]

# Step 2: Create CloudFront distribution
print("🌐 Creating CloudFront CDN...")
cloudfront_config = create_cloudfront_distribution(project_name, bucket)
distribution = cloudfront_config["distribution"]

# Step 3: Create bucket policy (allows CloudFront to access S3)
print("🔐 Configuring bucket policy...")
bucket_policy = create_bucket_policy(bucket, distribution.arn)

# Step 4: Upload website files
print("📤 Uploading website files...")
uploaded_files = upload_website_files(bucket, "website")

print("")
print("=" * 60)
print("✅ Deployment initiated!")
print("=" * 60)
print("")

# Export outputs
pulumi.export("bucket_name", bucket.id)
pulumi.export("bucket_website_endpoint", bucket.bucket.apply(
    lambda b: f"http://{b}.s3-website-us-east-1.amazonaws.com"
))
pulumi.export("cloudfront_url", distribution.domain_name.apply(
    lambda domain: f"https://{domain}"
))
pulumi.export("cloudfront_distribution_id", distribution.id)

# Next steps
pulumi.export("next_steps", [
    "",
    "✅ Deployment complete!",
    "",
    "🌐 Your website is live at:",
    "   https://<cloudfront_url> (see output above)",
    "",
    "📊 View outputs:",
    "   pulumi stack output cloudfront_url",
    "",
    "🔄 Update website content:",
    "   1. Edit files in website/ directory",
    "   2. Run: pulumi up",
    "   3. Wait for CloudFront to update (~5-10 min)",
    "",
    "🗑️  Invalidate CloudFront cache (force refresh):",
    "   aws cloudfront create-invalidation \\",
    "     --distribution-id <id> \\",
    "     --paths '/*'",
    "",
    "💰 Estimated cost: $0.00/month (Free Tier)",
    "",
])

print("🎉 Portfolio website deployment in progress!")
print("")
print("⏱️  CloudFront distribution takes 5-15 minutes to deploy")
print("📊 After deployment, run: pulumi stack output cloudfront_url")
print("")
