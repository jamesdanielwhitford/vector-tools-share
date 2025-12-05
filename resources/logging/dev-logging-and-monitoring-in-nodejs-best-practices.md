https://dev.to/imsushant12/logging-and-monitoring-in-nodejs-best-practices-2j1k

Logging and Monitoring in Node.js: Best Practices
=================================================

[#node](/t/node) [#javascript](/t/javascript) [#beginners](/t/beginners) [#webdev](/t/webdev)

[Backend with NodeJS (39 Part Series)](/imsushant12/series/28522)
-----------------------------------------------------------------

[1 Getting Started with NodeJS](/imsushant12/getting-started-with-node-js-4e1l "Published Aug 20 '24") [2 Deepening NodeJS Knowledge: URLs, HTTP Methods, Express Framework, and Versioning](/imsushant12/deepening-nodejs-knowledge-urls-http-methods-express-framework-and-versioning-3n0m "Published Aug 21 '24") [... 35 more parts...](/imsushant12/mastering-nodejs-rest-apis-middleware-and-http-headers-1l6n "View more") [3 Mastering NodeJS: REST APIs, Middleware, and HTTP Headers](/imsushant12/mastering-nodejs-rest-apis-middleware-and-http-headers-1l6n "Published Aug 22 '24") [4 Mastering Backend Development with NodeJS: MongoDB Integration, Mongoose, CRUD Operations, and MVC Architecture](/imsushant12/mastering-backend-development-with-nodejs-mongodb-integration-mongoose-crud-operations-and-mvc-architecture-36k4 "Published Aug 23 '24") [5 Securing Web Applications: Stateful vs. Stateless Systems, Authentication, and Authorization in Node.js](/imsushant12/securing-web-applications-stateful-vs-stateless-systems-authentication-and-authorization-in-nodejs-b1m "Published Aug 25 '24") [6 Mastering Web Development: Cookies, Authorization, Authentication, and File Uploads in Node.js](/imsushant12/mastering-web-development-cookies-authorization-authentication-and-file-uploads-in-nodejs-52j3 "Published Aug 27 '24") [7 Deploying and Scaling NodeJS Applications: A Comprehensive Guide](/imsushant12/deploying-and-scaling-nodejs-applications-a-comprehensive-guide-71o "Published Aug 28 '24") [8 Profiling and Benchmarking Node.js Applications](/imsushant12/profiling-and-benchmarking-nodejs-applications-2h2o "Published Sep 6 '24") [9 Advanced Memory Management and Garbage Collection in Node.js](/imsushant12/advanced-memory-management-and-garbage-collection-in-nodejs-4i51 "Published Sep 8 '24") [10 Mastering Event-Driven Programming with the EventEmitter in Node.js](/imsushant12/mastering-event-driven-programming-with-the-eventemitter-in-nodejs-38kd "Published Sep 10 '24") [11 Understanding Streams in Node.js — Efficient Data Handling](/imsushant12/understanding-streams-in-nodejs-efficient-data-handling-5e6l "Published Sep 12 '24") [12 Scaling Node.js Applications: Techniques and Best Practices](/imsushant12/scaling-nodejs-applications-techniques-and-best-practices-3lc0 "Published Sep 14 '24") [13 NGINX for Node.js Applications: What, Why, and How to Use It](/imsushant12/nginx-for-nodejs-applications-what-why-and-how-to-use-it-1gbn "Published Sep 16 '24") [14 Scaling Node.js Applications: Best Practices, Techniques, and Tools](/imsushant12/scaling-nodejs-applications-best-practices-techniques-and-tools-3406 "Published Sep 18 '24") [15 Understanding Node.js Streams: What, Why, and How to Use Them](/imsushant12/understanding-nodejs-streams-what-why-and-how-to-use-them-53da "Published Sep 20 '24") [16 Scaling Node.js Applications: Techniques, Tools, and Best Practices](/imsushant12/scaling-nodejs-applications-techniques-tools-and-best-practices-3344 "Published Sep 23 '24") [17 NGINX with Node.js: Load Balancing, Serving Static Content, and SSL](/imsushant12/nginx-with-nodejs-load-balancing-serving-static-content-and-ssl-29pb "Published Sep 25 '24") [18 WebSockets, Socket.IO, and Real-Time Communication with Node.js](/imsushant12/websockets-socketio-and-real-time-communication-with-nodejs-4ea0 "Published Sep 27 '24") [19 NGINX and Node.js - Serving Static Content and Handling SSL Encryption](/imsushant12/nginx-and-nodejs-serving-static-content-and-handling-ssl-encryption-13co "Published Sep 30 '24") [20 Real-time communication with WebSockets and Socket.IO in Node.js](/imsushant12/real-time-communication-with-websockets-and-socketio-in-nodejs-4p8e "Published Oct 2 '24") [21 Efficient Data Handling with Node.js Streams](/imsushant12/efficient-data-handling-with-nodejs-streams-4483 "Published Oct 4 '24") [22 Scaling Node.js Applications with NGINX and Load Balancing](/imsushant12/scaling-nodejs-applications-with-nginx-and-load-balancing-1a1d "Published Oct 7 '24") [23 WebSockets and Socket.IO: Real-Time Communication with Node.js](/imsushant12/websockets-and-socketio-real-time-communication-with-nodejs-2j5f "Published Oct 9 '24") [24 Node.js Streams: What, Why, and How to Use Them](/imsushant12/nodejs-streams-what-why-and-how-to-use-them-5d4f "Published Oct 11 '24") [25 Scaling Node.js Applications for High Performance](/imsushant12/scaling-nodejs-applications-for-high-performance-2d3b "Published Oct 14 '24") [26 Serving Static Content with NGINX](/imsushant12/serving-static-content-with-nginx-26ih "Published Oct 16 '24") [27 Understanding SSL, Encryption, and Their Importance in Web Applications](/imsushant12/understanding-ssl-encryption-and-their-importance-in-web-applications-45f0 "Published Oct 18 '24") [28 Scaling Node.js Applications: Strategies and Best Practices](/imsushant12/scaling-nodejs-applications-strategies-and-best-practices-a40 "Published Oct 21 '24") [29 Monitoring and Logging in Node.js Applications: Best Practices and Tools](/imsushant12/monitoring-and-logging-in-nodejs-applications-best-practices-and-tools-1llh "Published Oct 23 '24") [30 Security Best Practices for Node.js Applications](/imsushant12/security-best-practices-for-nodejs-applications-24mf "Published Oct 25 '24") [31 Performance Optimization Techniques for Node.js Applications](/imsushant12/performance-optimization-techniques-for-nodejs-applications-1jc2 "Published Oct 28 '24") [32 Effective Logging and Monitoring for Node.js Applications](/imsushant12/effective-logging-and-monitoring-for-nodejs-applications-2efl "Published Oct 30 '24") [33 A Guide for Securing Your Node.js Application](/imsushant12/a-guide-for-securing-your-nodejs-application-42cj "Published Nov 1 '24") [34 Database Optimization Techniques in Node.js](/imsushant12/database-optimization-techniques-in-nodejs-1la7 "Published Nov 4 '24") [35 Logging and Monitoring in Node.js: Best Practices](/imsushant12/logging-and-monitoring-in-nodejs-best-practices-2j1k "Published Nov 6 '24") [36 Deployment of a Node.js Application on AWS](/imsushant12/deployment-of-a-nodejs-application-on-aws-1pil "Published Nov 8 '24") [37 Working with WebSocket and Real-Time Communication in Node.js](/imsushant12/working-with-websocket-and-real-time-communication-in-nodejs-2ngg "Published Nov 11 '24") [38 Securing Node.js Applications: Best Practices and Strategies](/imsushant12/securing-nodejs-applications-best-practices-and-strategies-38c "Published Nov 13 '24") [39 Conclusion of My Node.js Journey and a Sneak Peek into My Upcoming AWS Series](/imsushant12/conclusion-of-my-nodejs-journey-and-a-sneak-peek-into-my-upcoming-aws-series-98l "Published Nov 15 '24")

Effective logging and monitoring are essential for maintaining application health, quickly identifying issues, and improving performance. In this article, we’ll dive into logging and monitoring for Node.js applications, covering key topics like choosing logging levels, setting up structured logs, integrating with monitoring tools, and best practices for using Winston and Elasticsearch.

[](#introduction-to-logging-and-monitoring)Introduction to Logging and Monitoring
---------------------------------------------------------------------------------

Logging helps capture real-time events, errors, and other important information from the application, while monitoring involves tracking application performance metrics over time. Together, they provide critical insights into application health, enabling proactive issue resolution.

[](#setting-up-basic-logging-in-nodejs)Setting Up Basic Logging in Node.js
--------------------------------------------------------------------------

The built-in `console` object provides simple logging functions, but a dedicated logging library is more robust for production applications.

### [](#basic-console-logging)Basic Console Logging

    console.log("Server started on port 3000");
    console.warn("This is a warning");
    console.error("Error occurred while processing request");
    

Enter fullscreen mode Exit fullscreen mode

However, console logging has limitations in complex applications, such as lack of log level control and no log persistence.

### [](#introducing-winston)Introducing Winston

Winston is a popular logging library for Node.js that offers multiple log levels, transports (log destinations), and structured logging.

1.  Install Winston:

       npm install winston
    

Enter fullscreen mode Exit fullscreen mode

1.  Setting Up Winston

       const winston = require("winston");
    
       // Configure logger
       const logger = winston.createLogger({
           level: "info",
           format: winston.format.combine(
               winston.format.timestamp(),
               winston.format.json()
           ),
           transports: [
               new winston.transports.Console(),
               new winston.transports.File({ filename: "app.log" })
           ]
       });
    
       // Logging examples
       logger.info("Server started on port 3000");
       logger.error("Database connection failed");
    

Enter fullscreen mode Exit fullscreen mode

[](#choosing-appropriate-log-levels)Choosing Appropriate Log Levels
-------------------------------------------------------------------

Log levels categorize log messages based on their importance. Common log levels are:

*   **Error**: Critical issues that require immediate attention, such as database or server failures.
*   **Warn**: Non-critical issues, such as deprecated APIs.
*   **Info**: General application information, like server startup or shutdown.
*   **Debug**: Detailed information useful during development, such as variable values.

### [](#configuring-log-levels-in-winston)Configuring Log Levels in Winston

    logger.level = "debug"; // Sets the minimum log level to debug, capturing all messages.
    

Enter fullscreen mode Exit fullscreen mode

In production, it’s best to keep log levels at `info` or `warn` to avoid unnecessary log data.

[](#structured-logging-for-consistency)Structured Logging for Consistency
-------------------------------------------------------------------------

Structured logging makes it easier to filter and analyze logs by maintaining a consistent format.

### [](#adding-metadata-to-logs)Adding Metadata to Logs

Metadata such as `user_id` or `request_id` can help track specific actions within logs:  

    logger.info("User login successful", { user_id: "12345" });
    logger.error("Failed to fetch user data", { user_id: "12345", error: "Database unavailable" });
    

Enter fullscreen mode Exit fullscreen mode

[](#integrating-with-elasticsearch-for-centralized-logging)Integrating with Elasticsearch for Centralized Logging
-----------------------------------------------------------------------------------------------------------------

Elasticsearch is widely used for centralized log management and search capabilities.

1.  **Install Elasticsearch and Elasticsearch Transport**

       npm install @elastic/elasticsearch winston-elasticsearch
    

Enter fullscreen mode Exit fullscreen mode

1.  **Configure Elasticsearch Transport**

       const { ElasticsearchTransport } = require("winston-elasticsearch");
    
       const esTransport = new ElasticsearchTransport({
           clientOpts: { node: "http://localhost:9200" }
       });
    
       logger.add(esTransport);
    

Enter fullscreen mode Exit fullscreen mode

This setup will send logs to Elasticsearch, allowing you to use Kibana for real-time log search and analysis.

[](#monitoring-application-metrics-with-prometheus-and-grafana)Monitoring Application Metrics with Prometheus and Grafana
-------------------------------------------------------------------------------------------------------------------------

Monitoring tracks application performance metrics like CPU usage, memory, and response times, helping to ensure a stable application.

### [](#setting-up-prometheus-with-nodejs)Setting Up Prometheus with Node.js

1.  **Install Prometheus Client Library**

       npm install prom-client
    

Enter fullscreen mode Exit fullscreen mode

1.  **Create and Export Metrics**

       const client = require("prom-client");
       const httpRequestDuration = new client.Histogram({
           name: "http_request_duration_seconds",
           help: "Duration of HTTP requests in seconds",
           labelNames: ["method", "route"]
       });
    
       function startMonitoring(req, res, next) {
           const end = httpRequestDuration.startTimer();
           res.on("finish", () => end({ method: req.method, route: req.path }));
           next();
       }
       app.use(startMonitoring);
    

Enter fullscreen mode Exit fullscreen mode

1.  **Expose Metrics Endpoint**

       app.get("/metrics", async (req, res) => {
           res.set("Content-Type", client.register.contentType);
           res.end(await client.register.metrics());
       });
    

Enter fullscreen mode Exit fullscreen mode

### [](#visualizing-with-grafana)Visualizing with Grafana

Grafana is a powerful tool for creating dashboards from Prometheus metrics. Integrate Prometheus as a data source in Grafana, then visualize metrics such as response times and error rates.

[](#realworld-use-case-logging-and-monitoring-in-ecommerce)Real-World Use Case: Logging and Monitoring in E-commerce
--------------------------------------------------------------------------------------------------------------------

Consider an e-commerce platform where logging and monitoring are critical for maintaining high performance and reliability.

1.  **Log All Transactions**: Capture order and payment events with structured logs, including metadata like `order_id` and `user_id`.
2.  **Error Tracking**: Use Winston to log errors such as payment failures, along with stack traces and metadata for faster debugging.
3.  **Monitor Server Health**: Set up Prometheus to monitor response times and request counts, visualized in Grafana for real-time insights.
4.  **Set Alerts**: Configure alerts based on metrics. For instance, if the request duration exceeds a threshold, send an alert to the admin.

This setup provides a comprehensive view of the application’s health, allowing proactive issue detection and resolution.

[](#conclusion)Conclusion
-------------------------

Implementing robust logging and monitoring in Node.js is essential for maintaining reliability and ensuring quick troubleshooting. Using tools like Winston, Elasticsearch, Prometheus, and Grafana, you can capture structured logs, centralize them, and monitor critical performance metrics effectively.

[Backend with NodeJS (39 Part Series)](/imsushant12/series/28522)
-----------------------------------------------------------------

[1 Getting Started with NodeJS](/imsushant12/getting-started-with-node-js-4e1l "Published Aug 20 '24") [2 Deepening NodeJS Knowledge: URLs, HTTP Methods, Express Framework, and Versioning](/imsushant12/deepening-nodejs-knowledge-urls-http-methods-express-framework-and-versioning-3n0m "Published Aug 21 '24") [... 35 more parts...](/imsushant12/mastering-nodejs-rest-apis-middleware-and-http-headers-1l6n "View more") [3 Mastering NodeJS: REST APIs, Middleware, and HTTP Headers](/imsushant12/mastering-nodejs-rest-apis-middleware-and-http-headers-1l6n "Published Aug 22 '24") [4 Mastering Backend Development with NodeJS: MongoDB Integration, Mongoose, CRUD Operations, and MVC Architecture](/imsushant12/mastering-backend-development-with-nodejs-mongodb-integration-mongoose-crud-operations-and-mvc-architecture-36k4 "Published Aug 23 '24") [5 Securing Web Applications: Stateful vs. Stateless Systems, Authentication, and Authorization in Node.js](/imsushant12/securing-web-applications-stateful-vs-stateless-systems-authentication-and-authorization-in-nodejs-b1m "Published Aug 25 '24") [6 Mastering Web Development: Cookies, Authorization, Authentication, and File Uploads in Node.js](/imsushant12/mastering-web-development-cookies-authorization-authentication-and-file-uploads-in-nodejs-52j3 "Published Aug 27 '24") [7 Deploying and Scaling NodeJS Applications: A Comprehensive Guide](/imsushant12/deploying-and-scaling-nodejs-applications-a-comprehensive-guide-71o "Published Aug 28 '24") [8 Profiling and Benchmarking Node.js Applications](/imsushant12/profiling-and-benchmarking-nodejs-applications-2h2o "Published Sep 6 '24") [9 Advanced Memory Management and Garbage Collection in Node.js](/imsushant12/advanced-memory-management-and-garbage-collection-in-nodejs-4i51 "Published Sep 8 '24") [10 Mastering Event-Driven Programming with the EventEmitter in Node.js](/imsushant12/mastering-event-driven-programming-with-the-eventemitter-in-nodejs-38kd "Published Sep 10 '24") [11 Understanding Streams in Node.js — Efficient Data Handling](/imsushant12/understanding-streams-in-nodejs-efficient-data-handling-5e6l "Published Sep 12 '24") [12 Scaling Node.js Applications: Techniques and Best Practices](/imsushant12/scaling-nodejs-applications-techniques-and-best-practices-3lc0 "Published Sep 14 '24") [13 NGINX for Node.js Applications: What, Why, and How to Use It](/imsushant12/nginx-for-nodejs-applications-what-why-and-how-to-use-it-1gbn "Published Sep 16 '24") [14 Scaling Node.js Applications: Best Practices, Techniques, and Tools](/imsushant12/scaling-nodejs-applications-best-practices-techniques-and-tools-3406 "Published Sep 18 '24") [15 Understanding Node.js Streams: What, Why, and How to Use Them](/imsushant12/understanding-nodejs-streams-what-why-and-how-to-use-them-53da "Published Sep 20 '24") [16 Scaling Node.js Applications: Techniques, Tools, and Best Practices](/imsushant12/scaling-nodejs-applications-techniques-tools-and-best-practices-3344 "Published Sep 23 '24") [17 NGINX with Node.js: Load Balancing, Serving Static Content, and SSL](/imsushant12/nginx-with-nodejs-load-balancing-serving-static-content-and-ssl-29pb "Published Sep 25 '24") [18 WebSockets, Socket.IO, and Real-Time Communication with Node.js](/imsushant12/websockets-socketio-and-real-time-communication-with-nodejs-4ea0 "Published Sep 27 '24") [19 NGINX and Node.js - Serving Static Content and Handling SSL Encryption](/imsushant12/nginx-and-nodejs-serving-static-content-and-handling-ssl-encryption-13co "Published Sep 30 '24") [20 Real-time communication with WebSockets and Socket.IO in Node.js](/imsushant12/real-time-communication-with-websockets-and-socketio-in-nodejs-4p8e "Published Oct 2 '24") [21 Efficient Data Handling with Node.js Streams](/imsushant12/efficient-data-handling-with-nodejs-streams-4483 "Published Oct 4 '24") [22 Scaling Node.js Applications with NGINX and Load Balancing](/imsushant12/scaling-nodejs-applications-with-nginx-and-load-balancing-1a1d "Published Oct 7 '24") [23 WebSockets and Socket.IO: Real-Time Communication with Node.js](/imsushant12/websockets-and-socketio-real-time-communication-with-nodejs-2j5f "Published Oct 9 '24") [24 Node.js Streams: What, Why, and How to Use Them](/imsushant12/nodejs-streams-what-why-and-how-to-use-them-5d4f "Published Oct 11 '24") [25 Scaling Node.js Applications for High Performance](/imsushant12/scaling-nodejs-applications-for-high-performance-2d3b "Published Oct 14 '24") [26 Serving Static Content with NGINX](/imsushant12/serving-static-content-with-nginx-26ih "Published Oct 16 '24") [27 Understanding SSL, Encryption, and Their Importance in Web Applications](/imsushant12/understanding-ssl-encryption-and-their-importance-in-web-applications-45f0 "Published Oct 18 '24") [28 Scaling Node.js Applications: Strategies and Best Practices](/imsushant12/scaling-nodejs-applications-strategies-and-best-practices-a40 "Published Oct 21 '24") [29 Monitoring and Logging in Node.js Applications: Best Practices and Tools](/imsushant12/monitoring-and-logging-in-nodejs-applications-best-practices-and-tools-1llh "Published Oct 23 '24") [30 Security Best Practices for Node.js Applications](/imsushant12/security-best-practices-for-nodejs-applications-24mf "Published Oct 25 '24") [31 Performance Optimization Techniques for Node.js Applications](/imsushant12/performance-optimization-techniques-for-nodejs-applications-1jc2 "Published Oct 28 '24") [32 Effective Logging and Monitoring for Node.js Applications](/imsushant12/effective-logging-and-monitoring-for-nodejs-applications-2efl "Published Oct 30 '24") [33 A Guide for Securing Your Node.js Application](/imsushant12/a-guide-for-securing-your-nodejs-application-42cj "Published Nov 1 '24") [34 Database Optimization Techniques in Node.js](/imsushant12/database-optimization-techniques-in-nodejs-1la7 "Published Nov 4 '24") [35 Logging and Monitoring in Node.js: Best Practices](/imsushant12/logging-and-monitoring-in-nodejs-best-practices-2j1k "Published Nov 6 '24") [36 Deployment of a Node.js Application on AWS](/imsushant12/deployment-of-a-nodejs-application-on-aws-1pil "Published Nov 8 '24") [37 Working with WebSocket and Real-Time Communication in Node.js](/imsushant12/working-with-websocket-and-real-time-communication-in-nodejs-2ngg "Published Nov 11 '24") [38 Securing Node.js Applications: Best Practices and Strategies](/imsushant12/securing-nodejs-applications-best-practices-and-strategies-38c "Published Nov 13 '24") [39 Conclusion of My Node.js Journey and a Sneak Peek into My Upcoming AWS Series](/imsushant12/conclusion-of-my-nodejs-journey-and-a-sneak-peek-into-my-upcoming-aws-series-98l "Published Nov 15 '24")

.long-bb-body { max-height: calc(100vh - 200px); overflow: hidden; } .long-bb-bottom { height: 180px; background: linear-gradient(to top, var(--card-bg), transparent); margin-top: -180px; position:relative; z-index: 5; }

[![profile](https://media2.dev.to/dynamic/image/width=64,height=64,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F140%2F9639a040-3c27-4b99-b65a-85e100016d3c.png)

MongoDB

](/mongodb)Promoted

Dropdown menu

*   [What's a billboard?](/billboards)
*   [Manage preferences](/settings/customization#sponsors)

* * *

*   [Report billboard](/report-abuse?billboard=238196)

[![Build seamlessly, securely, and flexibly with MongoDB Atlas. Try free.](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FVYTIlUE.png)](https://www.mongodb.com/cloud/atlas/lp/try3?utm_campaign=display_devto-webdev_pl_flighted_atlas_tryatlaslp_prosp_gic-null_ww-all_dev_dv-all_eng_leadgen&utm_source=devto&utm_medium=display&utm_content=runappsanywhere-v1&bb=238196)

[](#build-seamlessly-securely-and-flexibly-with-mongodb-atlas-try-free)[Build seamlessly, securely, and flexibly with MongoDB Atlas. Try free.](https://www.mongodb.com/cloud/atlas/lp/try3?utm_campaign=display_devto-webdev_pl_flighted_atlas_tryatlaslp_prosp_gic-null_ww-all_dev_dv-all_eng_leadgen&utm_source=devto&utm_medium=display&utm_content=runappsanywhere-v1&bb=238196)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MongoDB Atlas lets you build and run modern apps in 125+ regions across AWS, Azure, and Google Cloud. Multi-cloud clusters distribute data seamlessly and auto-failover between providers for high availability and flexibility. Start free!

[Learn More](https://www.mongodb.com/cloud/atlas/lp/try3?utm_campaign=display_devto-webdev_pl_flighted_atlas_tryatlaslp_prosp_gic-null_ww-all_dev_dv-all_eng_leadgen&utm_source=devto&utm_medium=display&utm_content=runappsanywhere-v1&bb=238196)

Read More

Top comments (0)
----------------

Subscribe

    ![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal Trusted User

[Create template](/settings/response-templates)

Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview [Dismiss](/404.html)

[Code of Conduct](/code-of-conduct) • [Report abuse](/report-abuse)

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](#).

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)