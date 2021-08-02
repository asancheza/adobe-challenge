# DevSecOps Technical Challenge

There are two challenges you should try and complete. Get as far as you can
and submit your results. During your panel you may be asked questions about
your work.

To submit your project, fork this repo and submit a PR. This PR should be
completed before the next in person phase of your interview.

## Coding Challenge

Using your preferred programming language (please avoid using bash, we tend
to use python for this sort of thing) grab the list of public Adobe repos
on github and print them into a table format from the command line. This
table should be sorted by most recently updated. In your table output, feel
free to include any fields that you think are useful. Perhaps number
of stargazers? 

To get you started, this endpoint gets you most of the repository data.

```bash
curl -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/adobe/repos
```

## Design Challenge

For the Design Challenge **choose one** of the options below.

For these options use concepts from any cloud you are familiar with or
Kubernetes. For example if you are familiar with Kubernetes use NetworkPolicy
to describe isolating a service with a firewall. If you are familiar with IBM
Cloud or AWS use security groups to do the same.

Your submission should at least include a design document in whatever easily
shareable format makes sense (PDF, PNG, jpeg, etc) and a document explaining
it. Use any diagramming software you like to lay out what is asked in each
challenge. If you are so inclined feel free to add supporting terraform
examples, code snippets, manifests, or any other technical resources to
 support your design.


### Option 1

Provide a design for an API endpoint that returns the string "Hello, Adobe!"
using functions as a service and any other services required to create that
system. Please consider security in your design while laying our your
architecture.

Include as much supporting documentation as needed to support your approach.

### Option 2

Provide the design for an HTTP based service that returns the simple HTML
message "Hello, Adobe!". This service will run in a container and should only
expose ports needed to be accessed via http/https.

In your design lay out how this container will run in the environment of your
choice and serve this endpoint, with security in mind. Also include
a description of what's running in the container or a Dockerfile.

For both please include any assumptions you make in your documentation.
