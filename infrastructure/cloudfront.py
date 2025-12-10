"""
CloudFront Distribution for Global CDN
Provides HTTPS, caching, and fast global delivery
"""
import pulumi
import pulumi_aws as aws

def create_cloudfront_distribution(project_name: str, bucket):
    """
    Create CloudFront distribution with Origin Access Control (OAC)
    """
    
    # Origin Access Control (OAC) - Modern way to secure S3 origin
    oac = aws.cloudfront.OriginAccessControl(
        f"{project_name}-oac",
        description=f"OAC for {project_name} S3 bucket",
        origin_access_control_origin_type="s3",
        signing_behavior="always",
        signing_protocol="sigv4",
    )
    
    # CloudFront Distribution
    distribution = aws.cloudfront.Distribution(
        f"{project_name}-cdn",
        enabled=True,
        is_ipv6_enabled=True,
        comment=f"{project_name} - Portfolio Website",
        default_root_object="index.html",
        
        # Origin configuration (S3 bucket)
        origins=[
            aws.cloudfront.DistributionOriginArgs(
                domain_name=bucket.bucket_regional_domain_name,
                origin_id=bucket.id,
                origin_access_control_id=oac.id,
            )
        ],
        
        # Default cache behavior
        default_cache_behavior=aws.cloudfront.DistributionDefaultCacheBehaviorArgs(
            allowed_methods=["GET", "HEAD", "OPTIONS"],
            cached_methods=["GET", "HEAD"],
            target_origin_id=bucket.id,
            
            # Forward settings
            forwarded_values=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesArgs(
                query_string=False,
                cookies=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs(
                    forward="none",
                ),
            ),
            
            # Viewer protocol policy (redirect HTTP to HTTPS)
            viewer_protocol_policy="redirect-to-https",
            
            # Compression
            compress=True,
            
            # TTL settings (cache for 1 hour)
            min_ttl=0,
            default_ttl=3600,
            max_ttl=86400,
        ),
        
        # Custom error responses
        custom_error_responses=[
            aws.cloudfront.DistributionCustomErrorResponseArgs(
                error_code=403,
                response_code=200,
                response_page_path="/index.html",
                error_caching_min_ttl=300,
            ),
            aws.cloudfront.DistributionCustomErrorResponseArgs(
                error_code=404,
                response_code=404,
                response_page_path="/404.html",
                error_caching_min_ttl=300,
            ),
        ],
        
        # Geographic restrictions (none)
        restrictions=aws.cloudfront.DistributionRestrictionsArgs(
            geo_restriction=aws.cloudfront.DistributionRestrictionsGeoRestrictionArgs(
                restriction_type="none",
            ),
        ),
        
        # SSL/TLS certificate (CloudFront default)
        viewer_certificate=aws.cloudfront.DistributionViewerCertificateArgs(
            cloudfront_default_certificate=True,
        ),
        
        # Price class (Use all edge locations for best performance)
        price_class="PriceClass_100",  # US, Canada, Europe (cheapest)
        
        # Tags
        tags={
            "Name": f"{project_name}-cdn",
            "Project": project_name,
        },
    )
    
    return {
        "distribution": distribution,
        "oac": oac,
    }
