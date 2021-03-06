<?php if(!class_exists('Rain\Tpl')){exit;}?><!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>

    <script type='application/ld+json'>
        [{
          '@context': 'http://schema.org/',
          '@type': 'Organization',
        
          // WARNING: Before sending email, either point the logo
          // at your own image or delete the logo annotation.
          //
          // If showing a logo, we recommend using an https URL.
          // It's not a requirement today, but may be in the future.
          'logo': 'https://www.gstatic.com/images/branding/product/1x/googleg_48dp.png'
        },{
          '@context': 'http://schema.org/',
          '@type': 'EmailMessage',
        
          // Use this optional alternative subject line to avoid duplicate text
          // between the subject, deal badge, and discount code.
          'subjectLine': '[Important] Please add subject line in annotation'
        },{
          '@context': 'http://schema.org/',
          '@type': 'DiscountOffer',
        
          // Describe your discount, this will be shown as a badge (eg '25% off' or 'free shipping')
          'description': '20% off',
        
          'discountCode': 'PROMO',
          'availabilityStarts': '2019-07-05T16:06:16-07:00',
          'availabilityEnds': '2019-07-08T16:06:16-07:00'
        },{
          // Promotion card with single image.
          // We recommend using an https URL.  It's not a requirement today, but may be in the future.
          // Any image size will work and will just be cropped automatically.
          // GIF & WEBP images are not supported and will be filtered out.
          // Sample image is 538x138, 3.9 aspect ratio
          '@context': 'http://schema.org/',
          '@type': 'PromotionCard',
          'image': 'https://www.google.com/gmail-for-marketers/promo-tab/markup-tool/sample.png'
        }]
            </script>

</head>
<body>
    <h1>
        Ola mundo, o <?php echo htmlspecialchars( $name, ENT_COMPAT, 'UTF-8', FALSE ); ?> é lindo!
    </h1>
</body>
</html>