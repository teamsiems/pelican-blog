Title: Network Expansion Equation
Date: 2009-07-14 13:54
Author: chris
Category: Personal
Tags: documentation, theory
Slug: a-universal-principle-in-routers
Status: published

<!-- wp:paragraph -->

*Several years ago, after I got my first router, I posted this on my Geocities page. Geocities is closing in October 2009, so I pulled it off and posted it here.*

<!-- /wp:paragraph -->

<!-- wp:image {"id":9544,"sizeSlug":"full","linkDestination":"none","align":"left"} -->

<figure class="wp-block-image alignleft size-full">
<img src="https://res.cloudinary.com/teamsiems/images/v1788444439/ai-generated-6a997f16aaad8/ai-generated-6a997f16aaad8.jpg?_i=AA" class="wp-image-9544" alt="Schematic diagram of a network modem" />
</figure>

<!-- /wp:image -->

<!-- wp:paragraph -->

I'm still struck by the profound notion of a universal principle, which I have to say was discovered by application of another universal principle, which again, relates to a not-so-universal principle. With me so far? I think this would be best illustrated through the use of an anecdote - so humor me for a moment and try to pay attention.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

One day I was starring at my computer-network's hardware, specifically the cable-modem and router. Then I was struck by the thought of what I remembered about the router: it can be 'daisy-chained' together with more routers - within a limit - to produce a massive network. I think logically in stream-of-consciousness thinking so what was my next logical thought. Of course, how many routers in a limit - or what is the limit. Well that was easy, 255. It said it in the manual. But, this wouldn't be a story if it ended there. I wondered 'how' to get to 255 and what is the significance of one path over another. Is one path more efficient than another? Check out my chicken scratch below for two possible daisy-chains.

<!-- /wp:paragraph -->

<!-- wp:html -->

<div class="clear">

</div>

<!-- /wp:html -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>

<!-- wp:paragraph -->

Here is an AI generated explanation.

<!-- /wp:paragraph -->

<!-- wp:heading -->

## Calculating Maximum Hub Capacity

<!-- /wp:heading -->

<!-- wp:paragraph -->

To determine the maximum number of hubs that can be connected to a single modem, we use a geometric series formula based on the number of expansion ports and the desired depth of the network hierarchy.

<!-- /wp:paragraph -->

<!-- wp:columns -->

<div class="wp-block-columns">

<!-- wp:column -->
</p>

<div class="wp-block-column">

<!-- wp:heading {"level":3} -->
</p>

### The Formula

<!-- /wp:heading -->

<!-- wp:paragraph -->

**H = M × ((P<sup>L</sup> - 1) / (P - 1))**

<!-- /wp:paragraph -->

</div>

<!-- /wp:column -->

<!-- wp:column -->

<div class="wp-block-column">

<!-- wp:heading {"level":3} -->
</p>

### Variables

<!-- /wp:heading -->

<!-- wp:list {"className":"wp-block-list"} -->

<ul class="wp-block-list">

<!-- wp:list-item -->
</p>

<li>

**H:** Total number of hubs
</li>

<!-- /wp:list-item -->

<!-- wp:list-item -->

<li>

**M:** Number of ports on the modem
</li>

<!-- /wp:list-item -->

<!-- wp:list-item -->

<li>

**P:** Expansion ports per hub (4)
</li>

<!-- /wp:list-item -->

<!-- wp:list-item -->

<li>

**L:** Number of network tiers (levels)
</li>

<!-- /wp:list-item -->

</ul>

<!-- /wp:list -->

</div>

<!-- /wp:column -->

</div>

<!-- /wp:columns -->

<!-- wp:paragraph {"className":"sg-ai-highlighted-block"} -->

For example, using a modem with 1 active port (M=1) and expanding to a depth of 3 tiers (L=3), the calculation is: (4³ - 1) / 3 = 21 total hubs.

<!-- /wp:paragraph -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>

<!-- wp:image {"id":9556,"sizeSlug":"full","linkDestination":"none","align":"left"} -->

<figure class="wp-block-image alignleft size-full">
<img src="https://res.cloudinary.com/teamsiems/images/v1788445579/ai-generated-6a99838a48b60/ai-generated-6a99838a48b60.jpg?_i=AA" class="wp-image-9556" alt="Technical diagram of a network topology" />
</figure>

<!-- /wp:image -->

<!-- wp:paragraph -->

My conclusion was that the chain with more routers should be less efficient, but what proof could I offer to justify this conclusion? Another mystery had arisen. A mystery which lead to this paper. My proof comes from the first universal principle: action = reaction (to paraphrase). Then I started thinking about this principle, and why I thought it was the answer. What I concluded (about my method of conclusion on the universal principle) is the not-so-universal principle: it seems reasonable because I cannot think of another explanation nor a contradiction. All I came up with were euphemisms or the same universal principle. A eureka moment. I realized that I had stumbled upon a universal principle. So am I wrong or do these phrases echo the same thought: equal and opposite reaction, yin and yang, give and take, do unto others as you would have them do unto you!

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

So, I can justify my conclusion by saying that more routers means more signals passing through the same ending wires (per second) means more collisions means less efficient; more take equals less give.

<!-- /wp:paragraph -->
