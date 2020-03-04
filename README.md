# bond-touch-interview

Bond Touch needs to a scalable HTTP api that writes raw data to
a data lake in AWS S3. The data stored here is about user behavior,
specifically about tracking which features are being used by each
user in order to understand what drives retention.

## Prompt and Challenge

### Technical Information

See the pdf file for an explanation of the architecture and costs.

See the swagger file for the HTTP spec.

### Interactions with us

You may ask us questions at any time. We will respond in one of two ways:

1. Answer the question directly. This is usually in the case where we should
   have been clear about something but were not.
2. Give a hint but not an answer. It is a good question but we would like to
   see how you figure it out without too much help.
3. Not answer or give a hint. In this case, we feel strongly that you should
   be able to figure out the answer on your own. You are not penalized in any
   way at all for asking one of these questions.

### Time

You will have 48 hours to do this test. It is not required for you to finish
everything, rather velocity is what is most important. In practical terms that
means you should do as much as possible in that time while recording how much 
time you spent on each task. Be honest in reporting the time you spent. If you 
lie about this you and we hire you, it will be discovered very quickly
resulting in a situation that is not fun for anybody.

## Evaluation Criteria

Don't second guess yourself while you are doing the test! Stay positive! and
do your best and report to us what you've done and let us judge the work! 
This is a hard challenge and it's important to keep a good state of mind. You 
are mostly going to be judged on how much you can get done in how much time. If 
you are able to do more because you have more time and re interested it will 
help but does not, by any means, guarantee that you'll get the job over 
someone who did the minimum requirements very quickly and efficiently.

### Basic Requirements

You should

- Implement an HTTP server using any technology you'd like.
- Implement the infrastructure in a one-off way by just using the
  AWS console. Clicking buttons FTW!
- Deploy the http server to the cloud.
- Everything (code, docs, etc.) are to be in version control. It's up to you
  how you'd like to organize it just as long as you can add me to a repo.
- Have some very basic tests showing the system works.
- Write good documentation

### Bonus

If you finish the above and want to move forward with bonus tasks to make
your application stand out, you may continue on to the following:

- Write a locustfile to stress test the http server
- Implement the infrastructure in terraform
- Encrypt the server with letsencrypt

## Additional Information

You are expected to already have or set up your own AWS account. You may be 
able to do everything within the free tier or you may have to spend a few euros. 
If you need to spend some money, let us know the estimate of it and we will
cover the costs by transfering the money to you directly.

I know this sounds like a strange requirement but as the first data scientist
/ data engineer at Bond Touch, you may very well end up doing these kinds
of tasks.

