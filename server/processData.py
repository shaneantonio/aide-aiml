from utils import insights_from_description, _insights_from_description, prepare_topic, get_today

if __name__ == "__main__":
    # print(insights_from_description(0))


    # mock_conv = [{"content": {"ai": "Hello Pandora, my name is AIDE, and I'm here to assist and chat with you. I heard you have a green thumb \u2013 any favorite memories from your gardens in the past that bring a smile to your face?"}}, {"content": {"human": "Oh, hello AIDE. Yes, I used to have the most beautiful roses in my garden. The colors were so vibrant. I remember spending hours tending to them."}}, {"content": {"ai": "That sounds wonderful, Pandora. Roses can be so enchanting. Do you recall any specific varieties or colors that were your absolute favorites?"}}, {"content": {"human": "Oh, I had these lovely red roses, deep red like rubies. But lately, I can't seem to remember their names. It's frustrating."}}, {"content": {"ai": "It's completely normal to forget details sometimes, Pandora. Your garden must have been a haven. Do you remember any other plants or flowers you enjoyed having in your garden?"}}, {"content": {"human": "Yes, I had some daisies too. Simple, but they brought a lot of joy. I'd arrange them in vases around the house."}}, {"content": {"ai": "Daisies are such cheerful flowers. Did you have a favorite spot in your garden where you liked to sit and enjoy the beauty around you?"}}, {"content": {"human": "Oh, yes. There was a little bench under the old oak tree. I'd sit there with a cup of tea and just watch the butterflies dance around. Lovely times."}}, {"content": {"ai": "That sounds like a peaceful retreat. The beauty of nature has a way of soothing the soul. Did you ever share this garden with friends or family?"}}, {"content": {"human": "Not so much. My husband used to join me sometimes. We'd have quiet afternoons together. But now, it's just me."}}, {"content": {"ai": "I'm sorry to hear that, Pandora. Gardens often hold precious memories. Is there anything specific you'd like to share or talk about regarding those times in your garden?"}}, {"content": {"human": "Well, lately, I find myself forgetting the names of the flowers and where certain plants were. It's frustrating. I want to keep those memories alive, you know?"}}, {"content": {"ai": "I understand, Pandora. It's completely normal to feel that way. Perhaps we can create a journal together, noting down the memories and details. That way, you can revisit them whenever you'd like."}}, {"content": {"human": "A journal? That's a good idea. It might help me remember things better. Thank you, AIDE."}}, {"content": {"ai": "You're welcome, Pandora. I'm here to help and chat whenever you feel like reminiscing or discussing anything else"}}]
    # print(_insights_from_description(mock_conv))

    print(prepare_topic(0, get_today()))
    # print(prepare_topic(0, "2023-11-20"))
    