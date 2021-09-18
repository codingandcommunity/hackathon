# == INCOMING TRANSMISSION ==

Agent, we have received the following messages from an asset embedded in the far-off nation of Narnia. An infamous band of thieves have stolen roughly $100 million from the Narnian bank, and it is up to you to return the money to its rightful owners.

We believe that the thieves have encoded the location of the money in the final message. However, they hashed their message with the MD5 algorithm, so we cannot get the location directly from this information. Fortunately, the other two messages provide clues on how to determine the location of the money.

The first message was most likely encoded with a Caesar cipher. It is up to you to determine the correct shift. Once you determine the shift, it should give you a message in plain English.

Next, the second message was most likely encoded with a substitution cipher. We know that the message begins with the phrase "THEMONEY" and that the vowels are encoded in the same way as the first message. For example, if "A" (decrypted) becomes "F" (encrypted) in the decoded first message, then you know that "A" (decrypted) becomes "F" (encrypted) in the second message as well.

Once you have cracked the second message, reverse it and run it through an MD5 hash. If you are correct, the hash will match the third message shown below and you will know the location of the $100 million.

Good luck, agent. The people of Narnia are depending on you.

```
== MESSAGE 1 (CAESAR CIPHER, UNKNOWN SHIFT) ==
MXWXCBQJANCQRBFRCQJWHXWN

== MESSAGE 2 (SUBSTITUTION CIPHER, STARTS WITH "THEMONEY", VOWELS AS IN MESSAGE 1) ==
VTNLXCNGRMRCVTNMTXNUXJ

== MESSAGE 3 (MD5 HASH OF REVERSED, DECRYPTED MESSAGE 2) ==
CALCULATE YOUR HASH HERE: https://www.md5hashgenerator.com/
fb541b750f6710e5e86ff7ef89c0ce24
```
