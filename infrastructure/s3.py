"""
S3 Bucket for Static Website Hosting
Configured to work with CloudFront
"""
import pulumi
import pulumi_aws as aws
import json

def create_s3_bucket(project_name: str):
    """
    Create S3 bucket for static website hosting with CloudFront
    """
    
    # S3 Bucket for website content
    bucket = aws.s3.Bucket(
        f"{project_name}-bucket",
        tags={
            "Name": f"{project_name}-bucket",
            "Project": project_name,
            "Purpose": "Static website hosting",
        }
    )
    
    # Block public access (CloudFront will access via OAC)
    aws.s3.BucketPublicAccessBlock(
        f"{project_name}-public-access-block",
        bucket=bucket.id,
        block_public_acls=True,
        block_public_policy=True,
        ignore_public_acls=True,
        restrict_public_buckets=True,
    )
    
    # Enable versioning (best practice)
    aws.s3.BucketVersioning(
        f"{project_name}-versioning",
        bucket=bucket.id,
        versioning_configuration=aws.s3.BucketVersioningVersioningConfigurationArgs(
            status="Enabled",
        ),
    )
    
    # Website configuration
    website_config = aws.s3.BucketWebsiteConfiguration(
        f"{project_name}-website-config",
        bucket=bucket.id,
        index_document=aws.s3.BucketWebsiteConfigurationIndexDocumentArgs(
            suffix="index.html",
        ),
        error_document=aws.s3.BucketWebsiteConfigurationErrorDocumentArgs(
            key="404.html",
        ),
    )
    
    return {
        "bucket": bucket,
        "website_config": website_config,
    }


def create_bucket_policy(bucket, cloudfront_distribution_arn):
    """
    Create bucket policy to allow CloudFront access
    """
    
    # Bucket policy allowing CloudFront OAC access
    bucket_policy = aws.s3.BucketPolicy(
        "bucket-policy",
        bucket=bucket.id,
        policy=pulumi.Output.all(bucket.arn, cloudfront_distribution_arn).apply(
            lambda args: json.dumps({
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "AllowCloudFrontServicePrincipal",
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "cloudfront.amazonaws.com"
                        },
                        "Action": "s3:GetObject",
                        "Resource": f"{args[0]}/*",
                        "Condition": {
                            "StringEquals": {
                                "AWS:SourceArn": args[1]
                            }
                        }
                    }
                ]
            })
        ),
    )
    
    return bucket_policy


def upload_website_files(bucket, website_dir: str = "website"):
    """
    Upload website files to S3 bucket
    """
    import os
    
    uploaded_files = []
    
    # Content type mapping
    content_types = {
        ".html": "text/html",
        ".css": "text/css",
        ".js": "application/javascript",
        ".json": "application/json",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
        ".ico": "image/x-icon",
        ".txt": "text/plain",
        ".pdf": "application/pdf",
    }
    
    # Walk through website directory and upload files
    for root, dirs, files in os.walk(website_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Get relative path from website_dir
            relative_path = os.path.relpath(file_path, website_dir)
            
            # Determine content type
            _, ext = os.path.splitext(file)
            content_type = content_types.get(ext.lower(), "application/octet-stream")
            
            # Upload file
            obj = aws.s3.BucketObject(
                f"file-{relative_path.replace('/', '-').replace('.', '-')}",
                bucket=bucket.id,
                key=relative_path.replace("\\", "/"),  # Normalize path for Windows
                source=pulumi.FileAsset(file_path),
                content_type=content_type,
                opts=pulumi.ResourceOptions(parent=bucket),
            )
            
            uploaded_files.append(obj)
    
    return uploaded_files
