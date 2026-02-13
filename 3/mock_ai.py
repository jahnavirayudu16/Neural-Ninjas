"""
Mock AI responses for testing and when Gemini quota is exceeded.
Provides plausible fashion styling recommendations.
"""

import random

def get_mock_recommendation(occasion, gender, favorite_colors='any', budget='mid', style_type='casual'):
    """Generate a mock outfit recommendation."""
    tops = {
        'male': ['crisp white shirt', 'navy polo', 'fitted t-shirt', 'casual blazer', 'linen shirt'],
        'female': ['blouse', 'crop top', 'fitted dress', 'casual sweater', 'silk camisole'],
        'other': ['button-up shirt', 'comfortable tee', 'stylish top', 'casual hoodie', 'fitted sweater']
    }
    
    bottoms = {
        'male': ['dark jeans', 'chinos', 'dress pants', 'casual trousers'],
        'female': ['skirt', 'jeans', 'dress pants', 'leggings', 'tailored trousers'],
        'other': ['jeans', 'trousers', 'dress pants', 'casual pants']
    }
    
    shoes = {
        'formal': ['dress shoes', 'heels', 'loafers', 'formal flats'],
        'casual': ['sneakers', 'trainers', 'slip-ons', 'casual boots'],
        'business': ['oxfords', 'pumps', 'loafers', 'professional flats'],
        'party': ['heels', 'dress shoes', 'elegant sandals', 'statement shoes'],
        'beach': ['sandals', 'flip-flops', 'water shoes', 'summer slides'],
        'default': ['comfortable shoes', 'trainers', 'casual footwear']
    }
    
    accessories = ['watch', 'belt', 'scarf', 'jewelry', 'sunglasses', 'hat', 'bag', 'backpack']
    
    tip_templates = [
        f"Layer with a light jacket for versatility.",
        f"Add a statement accessory to elevate your look.",
        f"Tuck in your top to create a defined silhouette.",
        f"Keep your color palette cohesive—use neutrals as your base.",
        f"Invest in quality basics that work across multiple outfits.",
        f"Play with proportions: if your top is loose, go fitted on the bottom.",
        f"Accessorize thoughtfully—less is more for a polished look.",
    ]
    
    gender_key = gender.lower() if gender.lower() in tops else 'other'
    shoe_key = occasion.lower() if occasion.lower() in shoes else 'default'
    
    top = random.choice(tops.get(gender_key, tops['other']))
    bottom = random.choice(bottoms.get(gender_key, bottoms['other']))
    shoe = random.choice(shoes.get(shoe_key, shoes['default']))
    acc = random.choice(accessories)
    tip = random.choice(tip_templates)
    
    recommendation = f"""
## Complete Outfit Recommendation for {occasion.capitalize()}

### Main Outfit
- **Top:** {top.capitalize()}
- **Bottom:** {bottom.capitalize()}
- **Shoes:** {shoe.capitalize()}

### Accessories
- Primary: {acc.capitalize()}
- Secondary: {random.choice(accessories).capitalize()}

### Color Coordination
Focus on your favorite colors: {favorite_colors}. Build a neutral base and add pops of color through accessories.

### Styling Tips
{tip}

### Budget Tips ({budget.capitalize()})
- Shop smart: look for quality pieces at reasonable prices
- Mix high and low: invest in a few key pieces, fill in with affordable basics
- Build a capsule wardrobe: choose versatile colors and styles

### Layering Ideas
Consider adding a cardigan, jacket, or scarf to add dimension and versatility to your outfit.

### Hairstyle Suggestions
Style your hair to complement your outfit. For a casual {occasion}, consider a relaxed style. For formal occasions, a more polished look works best.

_This recommendation was generated with care to match your style preferences!_
"""
    return recommendation.strip()


def get_mock_trends(region='global'):
    """Generate mock fashion trend insights."""
    trends = f"""
## Fashion Trends for {region.capitalize()} - 2026

### Trending Colors
- **Warm Neutrals:** Beige, cream, taupe remain strong
- **Jewel Tones:** Emerald, sapphire, and ruby are seeing a resurgence
- **Soft Pastels:** Blush pinks and sage greens dominate spring collections
- **Bold Accents:** Burnt orange and mustard for statement pieces

### Popular Silhouettes
- **Oversized Fits:** Relaxed, comfortable clothing continues
- **Maxi Styles:** Long skirts and dresses for elegance
- **Tailored Pieces:** Sharp lines for professional looks
- **Cargo & Utility:** Functional fashion with multiple pockets

### Trending Accessories
- **Mini Bags:** Tiny purses and crossbody bags
- **Statement Belts:** Wide belts with bold buckles
- **Chunky Jewelry:** Oversized chains and cuffs
- **Scarves:** Head wraps and silk scarves

### Fabrics & Materials
- **Sustainable Materials:** Organic cotton, linen, recycled fabrics
- **Leather:** Both vegan and traditional leather in neutral tones
- **Knits:** Oversized sweaters and cardigans
- **Sheer Fabrics:** Layering with transparency

### Budget-Friendly Trend Ideas
- Thrift stores are perfect for finding vintage pieces
- DIY customization of basic items
- Seasonal sales at major retailers
- Fast fashion chains offer trendy pieces at low prices

### Seasonal Recommendations
- **Spring:** Light fabrics, pastels, floral prints
- **Summer:** Breathable materials, bright colors, minimal coverage
- **Fall:** Earthy tones, layering, texture mix
- **Winter:** Dark colors, heavy fabrics, cozy knits

_Stay fashionable while honoring your personal style!_
"""
    return trends.strip()


def get_mock_image_analysis(filename):
    """Generate mock analysis for an uploaded image."""
    analysis = f"""
## Style Analysis for {filename}

### Color Palette
The outfit features a harmonious color scheme that's both versatile and flattering. The base color works well as a neutral, while accents add visual interest.

### Style Identification
**Primary Style:** Smart Casual  
**Secondary Influences:** Contemporary, Minimalist  
**Occasion Suitability:** Daytime, casual outings, social gatherings

### Matching Accessories Recommendations
- **Jewelry:** A delicate bracelet or small hoops would complement this look
- **Bag:** A structured tote or crossbody bag in a neutral tone
- **Belt:** An optional sleek belt to define the waist
- **Layers:** A lightweight cardigan or denim jacket

### Shoe Suggestions
1. **Comfortable Sneakers** - Perfect for a casual, laid-back vibe
2. **Loafers or Slip-ons** - Adds a touch of polish while staying comfortable
3. **Ankle Boots** - Great for creating visual interest and elongating the silhouette
4. **Sandals** - Ideal for warm weather styling

### Layering Ideas
- Add a kimono for a bohemian touch
- Layer with a denim or leather jacket for an edgier look
- Throw on a blazer for a more polished appearance
- Consider a cardigan for extra warmth and dimension

### Styling Improvements
1. **Color Coordination:** Consider pairing with complementary colors from the color wheel
2. **Proportions:** Ensure balance—if the top is loose, fit the bottom snugly
3. **Texture Mix:** Combine different materials for visual depth
4. **Accessory Strategy:** Keep accessories minimal or make one statement piece

### Occasions This Outfit Suits
✓ Casual coffee dates  
✓ Shopping or running errands  
✓ Brunch with friends  
✓ Casual workplace (depending on dress code)  
✓ Weekend hangouts  
✓ Travel and transportation  

### Additional Notes
Your outfit has great potential! The style is versatile and can be easily dressed up or down with the right accessories and footwear choices.

_Keep rocking your personal style!_
"""
    return analysis.strip()


def get_mock_chat_response(message):
    """Generate a mock response to a styling question."""
    responses = [
        "That's a great question! For a more cohesive look, I'd suggest focusing on a color palette with 2-3 main colors and building from there.",
        "Layering is key to creating versatile outfits. A well-fitted basic tee paired with a jacket can work for many occasions.",
        "Don't be afraid to mix patterns—just keep the scale different. A small print works well with a larger stripe!",
        "Accessories are your best friend! A statement belt or necklace can completely transform a simple outfit.",
        "Remember, the best outfit is one that makes YOU feel confident. Fashion rules are meant to be broken!",
        "Quality basics are worth the investment. A well-fitted pair of jeans and a neutral blazer go a long way.",
        "Thrift shopping is a fantastic way to find unique pieces while being budget-conscious. Have fun exploring!",
        "Color blocking—pairing bold, contrasting colors—is a fun way to make a statement. Just be confident!",
        "Comfort is key! If you don't feel comfortable wearing something, you won't feel confident either.",
        "Personal style evolves over time. Don't be afraid to try new things and discover what works for you!",
    ]
    return random.choice(responses)
