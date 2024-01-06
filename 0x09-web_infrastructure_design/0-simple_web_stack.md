
# Simple web stack

![](https://i.imgur.com/oCjInfP.jpeg)

## Server

A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network. In theory, whenever computers share resources with client machines they are considered servers.

## Domain name

**Domain name** is  a unique text-based/human-readable Internet address corresponding to a computer’s unique numeric IP address.

This is possible because of the DNS server process. Essentially, it begins by obtaining the domain name from the browser, and the ISP initiates the journey of figuring out its related IP. It starts by querying the DNS root server, which responds by providing the IP of the server containing details of the TLD (Top-Level Domain). Then, the resolver queries the TLD for the IP of the desired server.

DNS doesn't always contain the domain and its corresponding IP; that's just one of the many types that DNS has (that one called an A record). There is also the **CNAME** record, which is essentially like an alias to an A record. For example, the `www.foobar.com` is a **CNAME** record consisting of an indexing to the A record `foobar.com`. Basically, in the user's vision, these two domains are reaching the same location.
## Application server Vs. Web server

A **web server** accepts and fulfills requests from clients for static content (i.e., HTML pages, files, images, and videos) from a website. Web servers handle HTTP requests and responses _only_.

An **application server** exposes _business logic_ to the clients, which generates dynamic content. It is a software framework that transforms data to provide the specialized functionality offered by a business, service, or application. Application servers enhance the interactive parts of a website that can appear differently depending on the context of the request.

### Web Server

- Deliver static content
- Content is delivered using the HTTP protocol only.  
- Serves only web-based applications.
- No support for multi-threading.  
- Facilitates web traffic that is not very resource intensive.

### Application Server

- Delivers dynamic content.
- Provides business logic to application programs using several protocols (including HTTP).
- Can serve web and enterprise-based applications.
- Uses multi-threading to support multiple requests in parallel.
- Facilitates longer running processes that are very resource-intensive​
