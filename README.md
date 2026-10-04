# awesome-asyncio

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Libraries](https://img.shields.io/badge/libraries-496-FF7A28?labelColor=0F1E3D)](#libraries)
[![Updated](https://img.shields.io/badge/updated-2026--10--04-FF7A28?labelColor=0F1E3D)](#new-this-week)
[![License: CC0](https://img.shields.io/badge/license-CC0-FF7A28?labelColor=0F1E3D)](LICENSE)

Python libraries built on [asyncio](https://docs.python.org/3/library/asyncio.html) or that work with it, grouped by what they do. It is meant for browsing: you have a problem, you want to see what exists before picking one.

Every entry shows whether the repository is archived, when its last commit landed, its latest release and its star count. A script refreshes those numbers every Monday.

## Contents

- [New this week](#new-this-week)
- [Libraries](#libraries)
  - [Web frameworks](#web-frameworks) (36)
  - [ASGI servers](#asgi-servers) (5)
  - [HTTP clients](#http-clients) (26)
  - [WebSockets and realtime](#websockets-and-realtime) (8)
  - [GraphQL](#graphql) (7)
  - [RPC and serialization](#rpc-and-serialization) (10)
  - [Message queues and brokers](#message-queues-and-brokers) (20)
  - [Task queues and schedulers](#task-queues-and-schedulers) (14)
  - [Database drivers](#database-drivers) (46)
  - [ORMs and query builders](#orms-and-query-builders) (17)
  - [Networking](#networking) (44)
  - [Cloud and DevOps](#cloud-and-devops) (41)
  - [Files and I/O](#files-and-io) (13)
  - [Concurrency utilities](#concurrency-utilities) (44)
  - [Event loops](#event-loops) (5)
  - [Testing](#testing) (13)
  - [Observability and debugging](#observability-and-debugging) (12)
  - [Scraping and browser automation](#scraping-and-browser-automation) (16)
  - [Bots and chat](#bots-and-chat) (24)
  - [Auth and security](#auth-and-security) (8)
  - [CLI and TUI](#cli-and-tui) (4)
  - [IoT and hardware](#iot-and-hardware) (37)
  - [Alternatives to asyncio](#alternatives-to-asyncio) (7)
  - [Misc](#misc) (39)
- [How the data is collected](#how-the-data-is-collected)
- [Contributing](#contributing)
- [License](#license)

## New this week

Releases published and libraries added in the last 7 days. Older weeks are in [news/](news/), and there is an [Atom feed](feed.xml) if you prefer a reader.

**New releases**

| Library | Version | Date |
|---|---|---|
| [AsyncSSH](https://github.com/ronf/asyncssh) | 2.24.1 | 2026-10-04 |
| [Strawberry](https://github.com/strawberry-graphql/strawberry) | 0.330.3 | 2026-10-04 |
| [async-firebase](https://github.com/healthjoy/async-firebase) | 6.3.0 | 2026-10-04 |
| [websockets](https://github.com/python-websockets/websockets) | 17.2 | 2026-10-03 |
| [aiohomematic](https://github.com/SukramJ/aiohomematic) | 2026.10.3 | 2026-10-03 |
| [aiofranka](https://github.com/younghyopark/aiofranka) | 0.6.1 | 2026-10-03 |
| [aiotieba](https://github.com/lumina37/aiotieba) | 4.8.0 | 2026-10-02 |
| [asyncwhois](https://github.com/pogzyb/asyncwhois) | 1.1.15 | 2026-10-02 |
| [uvloop](https://github.com/MagicStack/uvloop) | 0.23.0 | 2026-10-01 |
| [aiobotocore](https://github.com/aio-libs/aiobotocore) | 3.9.2 | 2026-10-01 |
| [aiofastnet](https://github.com/aio-libs/aiofastnet) | 1.2.0 | 2026-10-01 |
| [FastAPI](https://github.com/fastapi/fastapi) | 0.142.2 | 2026-09-30 |
| [granian](https://github.com/emmett-framework/granian) | 2.8.4 | 2026-09-30 |
| [winloop](https://github.com/Vizonex/Winloop) | 0.7.0 | 2026-09-30 |
| [aioshelly](https://github.com/home-assistant-libs/aioshelly) | 13.34.1 | 2026-09-30 |
| [aioamazondevices](https://github.com/chemelli74/aioamazondevices) | 16.3.1 | 2026-09-30 |
| [aiormq](https://github.com/mosquito/aiormq) | 7.2.1 | 2026-09-29 |
| [Crawlee](https://github.com/apify/crawlee-python) | 1.10.3 | 2026-09-29 |
| [aiograpi](https://github.com/subzeroid/aiograpi) | 2.0.15 | 2026-09-29 |
| [aiounifi](https://github.com/Kane610/aiounifi) | 97 | 2026-09-29 |
| [asynckivy](https://github.com/asyncgui/asynckivy) | 0.12.0 | 2026-09-29 |
| [aio_energy_management](https://github.com/kotope/aio_energy_management) | 1.2.1 | 2026-09-29 |
| [aiomisc](https://github.com/aiokitchen/aiomisc) | 18.0.33 | 2026-09-28 |

## Libraries

Status: ✅ commit in the last year, 💤 no commit for over a year, 🗄️ archived on GitHub. Inside each group, archived projects come last and the rest are sorted by stars.

### Web frameworks

Frameworks and toolkits to build web apps and APIs.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [FastAPI](https://github.com/fastapi/fastapi) | API framework built on Starlette and Pydantic, driven by type hints | ✅ | 2026-10-02 | 0.142.2 | 102.8k |
| [Django](https://github.com/django/django) | An established, high-level Python web framework with a huge community and ecosystem | ✅ | 2026-10-03 | 6.1.1 | 91.3k |
| [Tornado](https://github.com/tornadoweb/tornado) | Performant web framework and asynchronous networking library | ✅ | 2026-10-04 | 6.5.10 | 22.2k |
| [sanic](https://github.com/sanic-org/sanic) | Web server and framework written for speed, with async request handling | ✅ | 2026-05-31 | 25.12.1 | 18.6k |
| [aiohttp](https://github.com/aio-libs/aiohttp) | Http client/server for asyncio (PEP-3156) | ✅ | 2026-10-04 | 3.14.3 | 16.6k |
| [Starlette](https://github.com/Kludex/starlette) | ASGI framework and toolkit for building web services | ✅ | 2026-10-04 | 1.7.0 | 12.7k |
| [django-ninja](https://github.com/vitalik/django-ninja) | Async-ready REST framework for Django, with type hints and Pydantic schemas | ✅ | 2026-10-04 | 1.7.1 | 9.2k |
| [Litestar](https://github.com/litestar-org/litestar) | Production-ready extensible ASGI framework with excellent performance and developer experience | ✅ | 2026-10-02 | 2.24.0 | 8.5k |
| [Quart](https://github.com/pallets/quart) | An asyncio web microframework with the same API as Flask | ✅ | 2026-09-12 | 0.23.1 | 3.7k |
| [asgiref](https://github.com/django/asgiref) | Backend utils for ASGI to WSGI integration, includes sync_to_async and async_to_sync function wrappers | ✅ | 2026-09-28 | 3.12.1 | 1.6k |
| [aiohttp-session](https://github.com/aio-libs/aiohttp-session) | Session management for aiohttp web applications | ✅ | 2026-10-01 | 2.12.1 | 245 |
| [aiohttp-jinja2](https://github.com/aio-libs/aiohttp-jinja2) | Jinja2 template rendering support for aiohttp web applications | ✅ | 2026-10-01 | 1.6 | 240 |
| [aiohttp-wsgi](https://github.com/etianen/aiohttp-wsgi) | WSGI adapter for aiohttp servers | 💤 | 2022-02-20 | 0.10.0 | 231 |
| [aiohttp-apispec](https://github.com/maximdanilchenko/aiohttp-apispec) | REST API documentation builder for aiohttp and apispec | 💤 | 2024-11-15 | 2.2.3 | 227 |
| [aiohttp-cors](https://github.com/aio-libs/aiohttp-cors) | CORS support middleware for aiohttp | ✅ | 2026-09-28 | 0.8.1 | 220 |
| [aiohttp-admin](https://github.com/aio-libs/aiohttp-admin) | Admin interface for aiohttp applications | ✅ | 2026-09-28 | v0.0.4 | 219 |
| [aiohttp-remotes](https://github.com/aio-libs/aiohttp-remotes) | Tools for aiohttp.web servers | ✅ | 2026-09-28 | 1.3.0 | 85 |
| [aiopyramid](https://github.com/housleyjk/aiopyramid) | Run Pyramid web framework with asyncio support | 💤 | 2022-09-16 | 0.4.1 | 78 |
| [aiohttp-pydantic](https://github.com/Maillol/aiohttp-pydantic) | Request validation with Pydantic for aiohttp | ✅ | 2026-09-23 | 3.0.2 | 75 |
| [aiohttp-swagger3](https://github.com/hh-h/aiohttp-swagger3) | OpenAPI 3.0 documentation and validation for aiohttp applications | 💤 | 2025-02-11 | 0.10.0 | 61 |
| [aiohttp-middlewares](https://github.com/playpauseandstop/aiohttp-middlewares) | Middleware collection for aiohttp web applications | ✅ | 2026-09-16 | 3.0.0 | 53 |
| [asynction](https://github.com/dedoussis/asynction) | SocketIO framework for asyncio driven by AsyncAPI specification | 💤 | 2022-05-03 | 0.8.3 | 51 |
| [aiohttp_validate](https://github.com/dchaplinsky/aiohttp_validate) | JSON schema validation library for aiohttp | ✅ | 2026-07-19 | 2.0 | 49 |
| [aiohttp-utils](https://github.com/sloria/aiohttp-utils) | Utility functions for aiohttp web development | 💤 | 2023-02-14 | 3.2.1 | 47 |
| [aiohttp-cache](https://github.com/cr0hn/aiohttp-cache) | Caching system for aiohttp server responses | ✅ | 2026-09-08 | 4.0.1 | 45 |
| [aiohttp_apiset](https://github.com/aamalev/aiohttp_apiset) | Swagger/OpenAPI specification-based routing for aiohttp | 💤 | 2025-03-22 | 0.9.18 | 41 |
| [AIOD-rest-api](https://github.com/aiondemand/AIOD-rest-api) | REST API services for AIoD metadata catalog and authentication | ✅ | 2026-08-06 | v2.1.20251113 | 37 |
| [aiorest-ws](https://github.com/Relrin/aiorest-ws) | REST framework with WebSocket support | 💤 | 2017-10-16 | 1.1.1 | 35 |
| [aiohttp-asgi](https://github.com/mosquito/aiohttp-asgi) | Run ASGI applications with aiohttp | 💤 | 2025-06-10 | 0.6.1 | 26 |
| [aiohttp-toolbox](https://github.com/samuelcolvin/aiohttp-toolbox) | Utility toolkit for aiohttp web development | 💤 | 2019-12-12 | 0.6.3 | 24 |
| [aiohttp_autoreload](https://github.com/anti1869/aiohttp_autoreload) | Auto-reload functionality for aiohttp server during development | 💤 | 2016-02-29 | 0.0.1 | 23 |
| [aiohttp_traversal](https://github.com/zzzsochi/aiohttp_traversal) | Traversal-based URL routing for aiohttp web applications | 💤 | 2018-10-31 | 0.11.0 | 20 |
| [aioflask](https://github.com/miguelgrinberg/aioflask) | Flask running on top of asyncio | 🗄️ | 2023-06-20 | 0.4.0 | 205 |
| [aio-openapi](https://github.com/quantmind/aio-openapi) | OpenAPI-compliant REST server framework with async support | 🗄️ | 2023-08-31 | 3.2.1 | 37 |
| [aiohttp-mako](https://github.com/aio-libs-abandoned/aiohttp-mako) | Mako template support for aiohttp web framework | 🗄️ | 2021-11-29 | v0.2.0 | 32 |
| [aiohttp_json_api](https://github.com/vovanbo/aiohttp_json_api) | JSON API implementation for aiohttp | 🗄️ | 2026-07-24 | 0.37.0 | 20 |

### ASGI servers

Servers that run asyncio web applications.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [uvicorn](https://github.com/Kludex/uvicorn) | ASGI server built on uvloop and httptools | ✅ | 2026-10-01 | 0.54.0 | 11.0k |
| [granian](https://github.com/emmett-framework/granian) | HTTP server for Python with a Rust core, supporting ASGI, RSGI and WSGI | ✅ | 2026-09-30 | 2.8.4 | 5.7k |
| [socketify](https://github.com/cirospaciari/socketify.py) | HTTP and WebSocket server for PyPy3 and Python 3, built on uWebSockets | ✅ | 2026-08-17 | 0.0.31 | 1.7k |
| [Hypercorn](https://github.com/pgjones/hypercorn) | ASGI server based on Hyper libraries and inspired by Gunicorn | ✅ | 2025-11-08 | 0.18.0 | 1.6k |
| [aiowsgi](https://github.com/gawel/aiowsgi) | Minimal WSGI server implementation using asyncio | 💤 | 2022-08-18 | 0.8 | 28 |

### HTTP clients

Async HTTP clients and request helpers.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [httpx](https://github.com/encode/httpx) | asynchronous HTTP client for Python 3 with requests compatible API | ✅ | 2026-02-23 | 0.28.1 | 15.5k |
| [aiohttp_retry](https://github.com/inyutin/aiohttp_retry) | Automatic retry mechanism for aiohttp requests | ✅ | 2026-04-08 | 2.9.1 | 272 |
| [aiohttp-socks](https://github.com/romis2012/aiohttp-socks) | SOCKS and HTTP proxy connector for aiohttp | ✅ | 2026-08-12 | 0.12.0 | 243 |
| [aiosonic](https://github.com/sonic182/aiosonic) | Fast HTTP and WebSocket client for asyncio | ✅ | 2026-09-28 | 1.0.7 | 170 |
| [aiohttp-client-cache](https://github.com/requests-cache/aiohttp-client-cache) | Async persistent cache for aiohttp requests | ✅ | 2026-10-01 | 0.14.3 | 155 |
| [asyncpraw](https://github.com/praw-dev/asyncpraw) | Async wrapper for Reddit API | ✅ | 2026-10-02 | 8.0.3 | 154 |
| [aiosteampy](https://github.com/somespecialone/aiosteampy) | Manage Steam sessions and trading with asyncio | ✅ | 2026-09-10 | 0.7.21 | 107 |
| [aioetherscan](https://github.com/ape364/aioetherscan) | Async wrapper for Etherscan blockchain API | 💤 | 2024-06-20 | 0.9.4 | 57 |
| [aiohttp-requests](https://github.com/maxzheng/aiohttp-requests) | Thin wrapper for aiohttp with requests-like API | 💤 | 2024-05-11 | 0.2.4 | 55 |
| [aiobungie](https://github.com/nxtlo/aiobungie) | Async Bungie API wrapper | ✅ | 2025-11-16 | 0.5.0 | 53 |
| [aiosfstream](https://github.com/robertmrk/aiosfstream) | Salesforce Streaming API client for asyncio | 💤 | 2019-03-08 | 0.5.0 | 46 |
| [aiohttp-ip-rotator](https://github.com/D4rkwat3r/aiohttp-ip-rotator) | Async IP rotation library for aiohttp | 💤 | 2025-01-10 | 1.0 | 45 |
| [Async-Poe-Client](https://github.com/canxin121/Async-Poe-Client) | Async client for poe.com | 💤 | 2023-09-27 | - | 45 |
| [async-batcher](https://github.com/hussein-awala/async-batcher) | HTTP request batching service for asyncio | 💤 | 2025-02-17 | 0.2.2 | 38 |
| [aiotractive](https://github.com/zhulik/aiotractive) | Async client for Tractive REST API | ✅ | 2026-10-03 | 1.0.3 | 37 |
| [async-stripe](https://github.com/bhch/async-stripe) | Async wrapper around Stripe official Python library | 💤 | 2023-12-03 | 6.1.0 | 37 |
| [aioaria2](https://github.com/synodriver/aioaria2) | Async wrapper for aria2-json-rpc | ✅ | 2026-08-22 | 1.3.7 | 36 |
| [aiogithubapi](https://github.com/ludeeus/aiogithubapi) | Async GitHub API client library | ✅ | 2026-07-18 | 26.0.0 | 29 |
| [aiosseclient](https://github.com/ebraminio/aiosseclient) | Async Server-Sent Events client | 💤 | 2025-03-12 | 0.1.8 | 28 |
| [aiocurl](https://github.com/fsbs/aiocurl) | Asyncio extension of PycURL library | 💤 | 2021-10-28 | 0.0.3.post1 | 28 |
| [asyncio-hn](https://github.com/itielshwartz/asyncio-hn) | Async wrapper for Hacker News API | 💤 | 2017-03-28 | 0.4.0 | 28 |
| [aiolinkding](https://github.com/bachya/aiolinkding) | Async interface to linkding bookmark API | 💤 | 2025-02-04 | 2025.2.0 | 25 |
| [aiopenapi3](https://github.com/commonism/aiopenapi3) | OpenAPI 3.0 client and validator with async/await support | ✅ | 2026-09-26 | 0.11.0 | 21 |
| [aiobravado](https://github.com/sjaensch/aiobravado) | Asyncio client for Swagger 2.0 services | 💤 | 2018-11-16 | 0.9.3 | 20 |
| [aiopolymarket](https://github.com/the-odds-company/aiopolymarket) | Type-safe async client for Polymarket API | ✅ | 2025-10-09 | - | 20 |
| [async-requests](https://github.com/inglesp/async-requests) | Async HTTP requests library | 💤 | 2014-05-17 | - | 20 |

### WebSockets and realtime

WebSocket, SSE and pub/sub libraries.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [websockets](https://github.com/python-websockets/websockets) | A library for building WebSocket servers and clients in Python with a focus on correctness and simplicity | ✅ | 2026-10-04 | 17.2 | 5.7k |
| [aiortc](https://github.com/aiortc/aiortc) | WebRTC and ORTC implementation using asyncio for real-time communication | ✅ | 2026-07-17 | 1.15.0 | 5.1k |
| [python-socketio](https://github.com/miguelgrinberg/python-socketio) | Socket.IO server and client for bidirectional real-time communication | ✅ | 2026-09-14 | 5.17.0 | 4.4k |
| [autobahn](https://github.com/crossbario/autobahn-python) | WebSocket and WAMP supporting asyncio and Twisted, for clients and servers | ✅ | 2026-09-29 | 26.7.1 | 2.5k |
| [aiowebsocket](https://github.com/asyncins/aiowebsocket) | Lightweight async WebSocket client library | 💤 | 2019-07-29 | 1.0.0.dev-2 | 317 |
| [aiohttp-sse](https://github.com/aio-libs/aiohttp-sse) | Server-sent events support for aiohttp | ✅ | 2026-10-01 | 2.2.0 | 238 |
| [aiohttp-sse-client](https://github.com/rtfol/aiohttp-sse-client) | Server-Sent Events (SSE) client library for aiohttp | 💤 | 2021-05-10 | 0.2.1 | 48 |
| [asyncio-sse](https://github.com/brutasse/asyncio-sse) | Server-Sent Events implementation for asyncio and aiohttp | 💤 | 2014-09-25 | 0.1 | 21 |

### GraphQL

Libraries to build and query GraphQL APIs.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [graphene](https://github.com/graphql-python/graphene) | GraphQL framework for Python with schema definition and query execution | 💤 | 2024-11-09 | 3.4.3 | 8.2k |
| [Strawberry](https://github.com/strawberry-graphql/strawberry) | Code-first Python 3 GraphQL server with Django, Flask and FastAPI/Starlette support | ✅ | 2026-10-04 | 0.330.3 | 4.7k |
| [Ariadne](https://github.com/mirumee/ariadne) | Schema-first Python library for implementing GraphQL servers | ✅ | 2026-08-31 | 1.1.0 | 2.3k |
| [Tartiflette](https://github.com/tartiflette/tartiflette) | Schema-first Python 3.6+ GraphQL engine built on top of libgraphqlparser | 💤 | 2022-01-20 | 1.4.1 | 854 |
| [aiohttp-graphql](https://github.com/graphql-python/aiohttp-graphql) | GraphQL support integration for aiohttp web applications | 💤 | 2020-08-07 | 1.1.0 | 117 |
| [aiographql-client](https://github.com/abn/aiographql-client) | GraphQL client for aiohttp | ✅ | 2026-09-21 | 2.0.0 | 30 |
| [aiogqlc](https://github.com/DoctorJohn/aiogqlc) | GraphQL client with async support, file uploads and subscriptions | ✅ | 2026-05-17 | 5.4.0 | 20 |

### RPC and serialization

gRPC, JSON-RPC and other remote call libraries.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [betterproto](https://github.com/danielgtaylor/python-betterproto) | Code generator and library for Protocol Buffers with async gRPC support | 💤 | 2025-07-17 | 1.2.5 | 1.8k |
| [grpclib](https://github.com/vmagamedov/grpclib) | Pure-Python gRPC implementation for asyncio with full protocol support | ✅ | 2025-12-14 | 0.4.9 | 988 |
| [fastapi-jsonrpc](https://github.com/smagafurov/fastapi-jsonrpc) | JSON-RPC 2.0 server framework built on FastAPI | ✅ | 2026-10-04 | 4.0.0 | 421 |
| [aiogrpc](https://github.com/hubo1016/aiogrpc) | Asyncio wrapper for gRPC | 💤 | 2020-08-24 | 1.8 | 114 |
| [aiorpc](https://github.com/choleraehyq/aiorpc) | Fast Python RPC library based on asyncio and MessagePack | 💤 | 2021-06-18 | 0.1.7 | 78 |
| [aiohttp-xmlrpc](https://github.com/mosquito/aiohttp-xmlrpc) | XML-RPC implementation for aiohttp | 💤 | 2022-12-18 | 1.5.0 | 34 |
| [aiorpcX](https://github.com/kyuupichan/aiorpcX) | Generic async RPC implementation | ✅ | 2026-02-19 | 0.25.0 | 30 |
| [aiohttp-rpc](https://github.com/michael-sulyak/aiohttp-rpc) | JSON-RPC 2.0 implementation for aiohttp | ✅ | 2026-01-19 | 2.0.0 | 28 |
| [aiohttp-json-rpc](https://github.com/pengutronix/aiohttp-json-rpc) | JSON-RPC 2.0 server implementation for aiohttp | 🗄️ | 2020-12-14 | 0.13.3 | 55 |
| [aiothrift](https://github.com/ryanwang520/aiothrift) | Thrift protocol support for asyncio | 🗄️ | 2026-01-05 | 0.2.7 | 43 |

### Message queues and brokers

Clients for AMQP, Kafka, NATS, ZeroMQ, MQTT and others.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [faststream](https://github.com/ag2ai/faststream) | Async client for Kafka, RabbitMQ, NATS, Redis and MQTT with AsyncAPI docs | ✅ | 2026-10-02 | 0.7.7 | 5.4k |
| [pyzmq](https://github.com/zeromq/pyzmq) | Python bindings for ZeroMQ | ✅ | 2026-08-20 | 27.2.0 | 4.2k |
| [crossbar](https://github.com/crossbario/crossbar) | Crossbar.io is a networking platform for distributed and microservice applications | ✅ | 2026-09-29 | 26.7.1 | 2.1k |
| [aio-pika](https://github.com/mosquito/aio-pika) | Asyncio wrapper for RabbitMQ built on aiormq for asyncio and humans | ✅ | 2026-09-27 | 10.1.0 | 1.5k |
| [aiokafka](https://github.com/aio-libs/aiokafka) | Client for Apache Kafka | ✅ | 2026-09-10 | 0.14.0 | 1.4k |
| [asyncio-nats](https://github.com/nats-io/nats.py) | Client for the NATS messaging system | ✅ | 2026-10-01 | 2.16.0 | 1.3k |
| [aiomqtt](https://github.com/empicano/aiomqtt) | Idiomatic asyncio MQTT client with type hints and async/await support | ✅ | 2026-04-23 | 2.5.1 | 575 |
| [aiozmq](https://github.com/aio-libs/aiozmq) | Alternative Asyncio integration with ZeroMQ | ✅ | 2026-03-26 | 1.0.0 | 431 |
| [aiormq](https://github.com/mosquito/aiormq) | Pure python AMQP asynchronous client library for asyncio | ✅ | 2026-09-29 | 7.2.1 | 318 |
| [aioamqp](https://github.com/Polyconseil/aioamqp) | AMQP implementation using asyncio | 💤 | 2022-04-05 | 0.15.0 | 282 |
| [aiomqtt](https://github.com/mossblaser/aiomqtt) | Async wrapper for paho-mqtt | 💤 | 2023-06-19 | - | 55 |
| [aioamqp_consumer](https://github.com/aio-libs/aioamqp_consumer) | Consumer, producer and RPC utilities built on aioamqp | 💤 | 2020-08-19 | 0.3.4 | 35 |
| [async_pubsub](https://github.com/abhinavsingh/async_pubsub) | Publish/Subscribe messaging using Redis, ZMQ and asyncio | 💤 | 2014-02-06 | 0.1.1 | 24 |
| [aiorabbit](https://github.com/gmr/aiorabbit) | RabbitMQ client library for asyncio | ✅ | 2026-08-31 | 1.0.3 | 23 |
| [aiostomp](https://github.com/pedrokiefer/aiostomp) | Async STOMP protocol client | 💤 | 2022-11-25 | 1.7.3 | 22 |
| [aionn](https://github.com/wrobell/aionn) | Async messaging library based on nanomsg | 💤 | 2018-10-09 | - | 22 |
| [aioconnectors](https://github.com/mori-b/aioconnectors) | Secure async message queue implementation | 💤 | 2024-07-01 | 1.6.3 | 21 |
| [aiomqttc](https://github.com/Tangerino/aiomqttc) | Async MQTT client for Python | 💤 | 2025-05-21 | 1.0.7 | 21 |
| [asynckafka](https://github.com/jmf-mordis/asynckafka) | Kafka client for asyncio | 🗄️ | 2021-01-23 | 0.2.0 | 34 |
| [Async-Channel](https://github.com/Drakkar-Software/Async-Channel) | Async multi-task communication library for concurrent operations | 🗄️ | 2026-01-03 | 2.2.2 | 21 |

### Task queues and schedulers

Background jobs, workers and cron-style scheduling.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [arq](https://github.com/python-arq/arq) | Job queues and background tasks with asyncio and Redis | ✅ | 2026-04-16 | 0.28.0 | 3.0k |
| [taskiq](https://github.com/taskiq-python/taskiq) | Asynchronous distributed task manager (like celery, but async) | ✅ | 2026-09-26 | 0.13.0 | 2.3k |
| [aiojobs](https://github.com/aio-libs/aiojobs) | Scheduler for managing background tasks with asyncio | ✅ | 2026-10-01 | 1.4.0 | 929 |
| [saq](https://github.com/tobymao/saq) | Distributed Python job queue with asyncio and redis architecture | ✅ | 2026-08-14 | 0.26.4 | 890 |
| [aiotasks](https://github.com/cr0hn/aiotasks) | Async task manager that distributes coroutines like Celery | ✅ | 2026-09-08 | 1.0.0 | 456 |
| [aiocron](https://github.com/gawel/aiocron) | Crontab-style job scheduling for asyncio applications | 💤 | 2025-09-28 | 2.1 | 377 |
| [aioclock](https://github.com/ManiMozaffar/aioclock) | Scheduling framework with dependency injection for asyncio | ✅ | 2026-09-13 | 0.3.0 | 243 |
| [streaq](https://github.com/tastyware/streaq) | Typed distributed task queue for asyncio, backed by Redis streams | ✅ | 2026-09-03 | 7.2.0 | 168 |
| [asyncmq](https://github.com/dymmond/asyncmq) | Asynchronous task queue framework | ✅ | 2026-09-04 | 0.10.1 | 80 |
| [asyncz](https://github.com/dymmond/asyncz) | Task scheduler and cron-like job executor for asyncio | ✅ | 2026-09-01 | 0.17.1 | 63 |
| [aio-celery](https://github.com/earlgreyness/aio-celery) | Celery worker for running asyncio coroutines | 💤 | 2025-06-23 | 0.22.0 | 61 |
| [aioworkers](https://github.com/aioworkers/aioworkers) | Configurable worker framework based on asyncio | 💤 | 2025-05-11 | 0.28.0 | 46 |
| [aioscheduler](https://github.com/Gelbpunkt/aioscheduler) | Scalable task scheduler for asyncio | 💤 | 2020-10-02 | 1.4.2 | 30 |
| [async_cron](https://github.com/aohan237/async_cron) | Crontab scheduler for Python asyncio | ✅ | 2025-10-29 | 1.6.2 | 29 |

### Database drivers

Async drivers for SQL, NoSQL, search and time-series databases.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [redis-py](https://github.com/redis/redis-py) | Redis Python Client (which includes aioreadis now) | ✅ | 2026-10-04 | 8.1.0 | 13.6k |
| [asyncpg](https://github.com/MagicStack/asyncpg) | PostgreSQL client library for asyncio | ✅ | 2026-10-03 | 0.31.0 | 8.1k |
| [pymongo](https://github.com/mongodb/mongo-python-driver) | The Official MongoDB Python driver, offering both synchronous and asynchronous APIs | ✅ | 2026-10-02 | 4.18.2 | 4.4k |
| [motor](https://github.com/mongodb/motor) | Non-blocking MongoDB driver for asyncio and Tornado with native async/await | ✅ | 2026-09-30 | 3.7.1 | 2.5k |
| [aiomysql](https://github.com/aio-libs/aiomysql) | Library for accessing a MySQL database | ✅ | 2025-12-22 | 0.3.2 | 1.9k |
| [aiosqlite](https://github.com/omnilib/aiosqlite) | Asyncio bridge to the standard sqlite3 module with complete async interface | ✅ | 2025-12-23 | 0.22.1 | 1.6k |
| [aiopg](https://github.com/aio-libs/aiopg) | Library for accessing a PostgreSQL database | ✅ | 2025-12-03 | 1.4.0 | 1.4k |
| [aiosql](https://github.com/nackjicholson/aiosql) | Execute SQL queries asynchronously using asyncio | ✅ | 2026-07-10 | 15.0 | 1.4k |
| [asyncio-redis](https://github.com/jonathanslenders/asyncio-redis) | Redis client library for Python asyncio | 💤 | 2020-08-11 | 0.16.0 | 549 |
| [asyncpgsa](https://github.com/CanopyTax/asyncpgsa) | Asyncpg with sqlalchemy core support | 💤 | 2021-02-26 | 0.27.1 | 505 |
| [aiosqlitepool](https://github.com/slaily/aiosqlitepool) | Connection pool for async SQLite operations | 💤 | 2025-07-21 | 1.0.0 | 431 |
| [asyncmy](https://github.com/long2ice/asyncmy) | The fastest asyncio MySQL/MariaDB driver for Python with pure async design | ✅ | 2026-09-25 | 0.2.15 | 391 |
| [aioodbc](https://github.com/aio-libs/aioodbc) | Library for accessing a ODBC databases | 💤 | 2023-10-28 | 0.5.0 | 325 |
| [aiochclient](https://github.com/maximdanilchenko/aiochclient) | Lightweight async HTTP ClickHouse client with type conversion | ✅ | 2026-06-08 | 2.7.0 | 257 |
| [asynch](https://github.com/long2ice/asynch) | Asyncio ClickHouse client with TCP interface | ✅ | 2026-08-14 | 0.4.0 | 244 |
| [aioch](https://github.com/mymarilyn/aioch) | ClickHouse database driver for asyncio | 💤 | 2022-02-27 | 0.0.2 | 169 |
| [aiomcache](https://github.com/aio-libs/aiomcache) | Minimal asyncio memcached client | ✅ | 2026-09-01 | 0.8.2 | 158 |
| [AsyncTorndb](https://github.com/mayflaver/AsyncTorndb) | Async MySQL client for Tornado with asyncio support | 💤 | 2016-01-06 | - | 157 |
| [aioelasticsearch](https://github.com/aio-libs/aioelasticsearch) | Async client for Elasticsearch | 💤 | 2022-01-22 | 0.7.0 | 137 |
| [aiodynamo](https://github.com/HENNGE/aiodynamo) | Asynchronous DynamoDB client with Pythonic API | ✅ | 2026-07-03 | 26.4 | 94 |
| [asynctnt](https://github.com/igorcoding/asynctnt) | Async connector for Tarantool database | 💤 | 2024-12-01 | 2.4.0 | 83 |
| [aiotinydb](https://github.com/aiotinydb/aiotinydb) | Asyncio compatibility wrapper for TinyDB | 💤 | 2023-01-29 | 2.0.0 | 75 |
| [AsyncDB](https://github.com/JimChengLin/AsyncDB) | In-memory async database implementation with B-Tree structure | 💤 | 2019-05-20 | - | 66 |
| [asyncdb](https://github.com/phenobarbital/asyncdb) | Generic asynchronous database connectors for multiple backends | ✅ | 2026-09-14 | 2.16.2 | 55 |
| [aiocouchdb](https://github.com/aio-libs/aiocouchdb) | CouchDB client built on top of aiohttp (asyncio) | 💤 | 2016-09-12 | 0.9.1 | 54 |
| [asyncpg-listen](https://github.com/anna-money/asyncpg-listen) | Simplify PostgreSQL LISTEN notifications with asyncpg | ✅ | 2026-05-31 | 0.0.9 | 47 |
| [aiogremlin](https://github.com/davebshow/aiogremlin) | Async Gremlin client for Python | 💤 | 2018-03-27 | 3.3.4 | 43 |
| [aiotarantool](https://github.com/shveenkov/aiotarantool) | Asynchronous connector for Tarantool database | 💤 | 2019-12-11 | 1.1.5 | 40 |
| [aioetcd3](https://github.com/gaopeiliang/aioetcd3) | Async etcd3 client | 💤 | 2020-09-30 | 1.13 | 35 |
| [aiocouch](https://github.com/metricq/aiocouch) | Async client library for CouchDB NoSQL database | 💤 | 2025-07-11 | 4.0.1 | 34 |
| [async-flask-sqlalchemy-postgresql](https://github.com/sixu05202004/async-flask-sqlalchemy-postgresql) | Async PostgreSQL database connector | 💤 | 2014-03-21 | - | 34 |
| [aioneo4j](https://github.com/aio-libs/aioneo4j) | Asynchronous client driver for Neo4j graph database | 💤 | 2022-01-23 | - | 28 |
| [aiosparql](https://github.com/aio-libs/aiosparql) | SPARQL query client for asyncio using aiohttp | 💤 | 2021-02-27 | 0.12.0 | 24 |
| [aioredis-cluster](https://github.com/DriverX/aioredis-cluster) | Redis Cluster support extension for aioredis | 💤 | 2023-12-18 | 2.7.0 | 24 |
| [aiohappybase](https://github.com/python-happybase/aiohappybase) | Asyncio fork of HappyBase for HBase access | 💤 | 2021-02-02 | 1.4.0 | 22 |
| [aiossdb](https://github.com/Microndgt/aiossdb) | SSDB database client driver for asyncio | 💤 | 2017-08-22 | 0.0.5 | 21 |
| [aiotrino](https://github.com/mvanderlee/aiotrino) | Async Trino SQL client | 💤 | 2025-03-21 | 0.3.0 | 21 |
| [aioetcd](https://github.com/lisael/aioetcd) | Async etcd client | 💤 | 2014-12-18 | - | 20 |
| [aioredis-py](https://github.com/aio-libs-abandoned/aioredis-py) | Asyncio client for Redis | 🗄️ | 2022-02-22 | v2.0.1 | 2.3k |
| [asyncmongo](https://github.com/bitly/asyncmongo) | Async library for accessing MongoDB with tornado.ioloop | 🗄️ | 2014-05-20 | 1.3 | 606 |
| [aioinflux](https://github.com/gusutabopb/aioinflux) | InfluxDB client built on top of aiohttp | 🗄️ | 2023-08-05 | 0.9.0 | 162 |
| [aioinflux](https://github.com/gusutabopb/aioinflux) | Async client library for InfluxDB time-series database | 🗄️ | 2023-08-05 | 0.9.0 | 162 |
| [aioes](https://github.com/aio-libs-abandoned/aioes) | Asyncio compatible driver for elasticsearch | 🗄️ | 2017-08-22 | 0.7.2 | 99 |
| [aioes](https://github.com/aio-libs-abandoned/aioes) | Elasticsearch client driver for asyncio | 🗄️ | 2017-08-22 | v0.7.1 | 99 |
| [aiocassandra](https://github.com/aio-libs/aiocassandra) | Cassandra database driver for asyncio | 🗄️ | 2019-04-23 | 2.0.1 | 85 |
| [asyncflux](https://github.com/puentesarrin/asyncflux) | Async client for InfluxDB | 🗄️ | 2015-02-26 | - | 25 |

### ORMs and query builders

Object mappers and query builders on top of async drivers.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [Tortoise ORM](https://github.com/tortoise/tortoise-orm) | native multi-backend ORM with Django-like API and easy relations management | ✅ | 2026-10-03 | 1.1.8 | 5.6k |
| [GINO](https://github.com/python-gino/gino) | is a lightweight asynchronous Python ORM based on SQLAlchemy core, with asyncpg dialect | 💤 | 2022-02-12 | 1.0.1 | 2.8k |
| [Beanie](https://github.com/BeanieODM/beanie) | An async MongoDB ODM built on pymongo and Pydantic | ✅ | 2026-08-31 | 2.2.0 | 2.7k |
| [Piccolo](https://github.com/piccolo-orm/piccolo) | An ORM / query builder which can work in async and sync modes, with a nice admin GUI, and ASGI middleware | ✅ | 2026-09-14 | 1.36.0 | 1.9k |
| [ormar](https://github.com/ormar-orm/ormar) | Async ORM with fastapi in mind, pydantic validation and relational support | ✅ | 2026-10-02 | 0.26.0 | 1.8k |
| [odmantic](https://github.com/art049/odmantic) | Sync and async ODM for MongoDB based on python type hints and pydantic | ✅ | 2026-01-25 | 1.1.0 | 1.2k |
| [oxyde](https://github.com/mr-fatalyst/oxyde) | Async ORM for Python with a Rust core | ✅ | 2026-09-29 | 0.8.0 | 763 |
| [peewee-async](https://github.com/05bit/peewee-async) | ORM implementation based on peewee and aiopg | ✅ | 2026-08-28 | 2.1.0 | 762 |
| [edgy](https://github.com/dymmond/edgy) | Perfect ORM for complex database queries with full async/await support | ✅ | 2026-09-29 | 0.37.0 | 440 |
| [asyncorm](https://github.com/monobot/asyncorm) | Fully asynchronous ORM inspired by Django with async/await support | 💤 | 2020-08-20 | 0.5.3 | 174 |
| [aiopeewee](https://github.com/kszucs/aiopeewee) | Asyncio integration for Peewee ORM | 💤 | 2020-04-29 | 0.4.2 | 46 |
| [asyncom](https://github.com/vinissimus/asyncom) | Asynchronous Python object mapper for database operations | 💤 | 2022-06-22 | 0.3.3 | 35 |
| [aiopyql](https://github.com/codemation/aiopyql) | Async ORM for RDBMS with Python | 💤 | 2021-05-21 | 0.359 | 34 |
| [aiomotorengine](https://github.com/ilex/aiomotorengine) | Motor/MotorEngine compatibility ORM for asyncio | 💤 | 2025-05-20 | - | 27 |
| [asyncmongo-orm](https://github.com/marcelnicolay/asyncmongo-orm) | Object-relational mapping for asyncmongo | 💤 | 2012-05-07 | - | 27 |
| [Databases](https://github.com/encode/databases) | Async database access for SQLAlchemy core, with support for PostgreSQL, MySQL, and SQLite | 🗄️ | 2024-03-01 | 0.9.0 | 4.0k |
| [Prisma Client Python](https://github.com/RobertCraigie/prisma-client-py) | Type-safe ORM generated from your schema, for SQLite, PostgreSQL, MySQL and MongoDB | 🗄️ | 2025-03-23 | 0.15.0 | 2.1k |

### Networking

DNS, SSH, ping, sockets and protocol implementations.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [aioquic](https://github.com/aiortc/aioquic) | QUIC and HTTP/3 protocol implementation in Python | ✅ | 2025-10-11 | 1.3.0 | 2.0k |
| [AsyncSSH](https://github.com/ronf/asyncssh) | Provides an asynchronous client and server implementation of the SSHv2 protocol | ✅ | 2026-10-04 | 2.24.1 | 1.8k |
| [aiodnsbrute](https://github.com/blark/aiodnsbrute) | Async DNS brute force utility for discovering DNS records | 💤 | 2019-06-04 | 0.3.2 | 674 |
| [aiodns](https://github.com/aio-libs/aiodns) | DNS resolver for asyncio built on pycares | ✅ | 2026-09-28 | 4.0.4 | 592 |
| [aiocoap](https://github.com/chrysn/aiocoap) | Constrained Application Protocol (CoAP) library for asyncio | ✅ | 2026-04-24 | 0.4.17 | 293 |
| [aiosmb](https://github.com/skelsec/aiosmb) | Asynchronous SMB (Server Message Block) client library | ✅ | 2026-08-14 | 0.4.14 | 220 |
| [aioftp](https://github.com/aio-libs/aioftp) | FTP client and server for asyncio | ✅ | 2026-09-19 | 0.28.3 | 211 |
| [asyncio-socks-server](https://github.com/Amaindex/asyncio-socks-server) | SOCKS5 server with asynchronous Python hooks | ✅ | 2026-08-25 | 1.3.3 | 183 |
| [aioimaplib](https://github.com/iroco-co/aioimaplib) | Asyncio IMAP4rev1 client library | ✅ | 2026-09-24 | - | 170 |
| [aioice](https://github.com/aiortc/aioice) | Asyncio implementation of Interactive Connectivity Establishment | ✅ | 2026-03-18 | 0.10.2 | 141 |
| [async_rithmic](https://github.com/rundef/async_rithmic) | Async client for Rithmic Protocol Buffer API | ✅ | 2026-08-21 | 1.6.6 | 120 |
| [aiosocks](https://github.com/nibrag/aiosocks) | SOCKS proxy client implementation for asyncio | 💤 | 2020-04-13 | 0.2.6 | 118 |
| [asyncmcp](https://github.com/bh-rat/asyncmcp) | Async transport layers for MCP | ✅ | 2026-05-08 | 0.2.1 | 109 |
| [asyncwhois](https://github.com/pogzyb/asyncwhois) | Async WHOIS and RDAP client for domain information | ✅ | 2026-10-02 | 1.1.15 | 100 |
| [aioping](https://github.com/stellarbit/aioping) | Asyncio implementation of the ICMP ping protocol | 💤 | 2023-07-11 | 0.4.0 | 92 |
| [aiosip](https://github.com/Eyepea/aiosip) | SIP protocol support for asyncio | 💤 | 2020-12-21 | 0.2.0 | 86 |
| [aionion](https://github.com/ultrafunkamsterdam/aionion) | Proxy pool with request rotation for requests and aiohttp | 💤 | 2023-03-04 | - | 84 |
| [aioh2](https://github.com/decentfox/aioh2) | HTTP/2 implementation for asyncio | 💤 | 2023-10-15 | 0.2.3 | 78 |
| [async_dns](https://github.com/gera2ld/async_dns) | DNS resolver library built on asyncio | ✅ | 2026-07-25 | 2.0.1 | 74 |
| [aioslsk](https://github.com/JurgenR/aioslsk) | SoulSeek client library using asyncio | ✅ | 2026-10-03 | 1.6.4 | 66 |
| [aiodnsresolver](https://github.com/michalc/aiodnsresolver) | DNS resolver implementation for asyncio | 💤 | 2025-01-07 | 0.0.157 | 63 |
| [aiortsp](https://github.com/marss/aiortsp) | RTSP library using asyncio | 💤 | 2024-09-27 | 1.4.0 | 57 |
| [asyncio-dgram](https://github.com/jsbronder/asyncio-dgram) | Higher level UDP datagram support for asyncio | ✅ | 2026-01-21 | 3.0.0 | 56 |
| [aiohappyeyeballs](https://github.com/aio-libs/aiohappyeyeballs) | Happy Eyeballs IPv4/IPv6 connection algorithm for asyncio | ✅ | 2026-07-25 | 2.7.1 | 46 |
| [aiofastnet](https://github.com/aio-libs/aiofastnet) | Ultra-fast TCP networking with kernel TLS for asyncio | ✅ | 2026-10-01 | 1.2.0 | 35 |
| [asyncudp](https://github.com/eerimoq/asyncudp) | Asyncio high level UDP sockets | 💤 | 2023-07-24 | 0.11.0 | 34 |
| [aiotunnel](https://github.com/codepr/aiotunnel) | HTTP tunnel implementation using aiohttp and asyncio | 💤 | 2020-07-07 | - | 33 |
| [aiostratum_proxy](https://github.com/wetblanketcc/aiostratum_proxy) | Modular Stratum mining proxy protocol implementation | 💤 | 2018-10-07 | 1.1 | 31 |
| [aiobtdht](https://github.com/bashkirtsevich-llc/aiobtdht) | Async BitTorrent DHT server implementation | 💤 | 2023-11-01 | - | 28 |
| [aioax25](https://github.com/sjlongland/aioax25) | Asynchronous AX.25 protocol library | ✅ | 2026-06-14 | 0.0.11.post0 | 27 |
| [aiodav](https://github.com/jorgeajimenezl/aiodav) | Async WebDAV client | 💤 | 2025-09-05 | 0.1.14 | 27 |
| [aioudp](https://github.com/bashkirtsevich-llc/aioudp) | Async UDP server implementation | 💤 | 2024-07-30 | 0.0.7 | 26 |
| [aioupnp](https://github.com/lbryio/aioupnp) | Universal Plug and Play (UPnP) protocol support for asyncio | 💤 | 2020-12-21 | 0.0.18 | 26 |
| [aiotorrent](https://github.com/Mys7erio/aiotorrent) | Asynchronous BitTorrent client library in pure Python | ✅ | 2025-10-05 | 0.9.2 | 26 |
| [aiodns](https://github.com/vshymanskyy/aiodns) | Async DNS client for MicroPython | ✅ | 2026-08-05 | - | 26 |
| [aiorcon](https://github.com/skmendez/aiorcon) | Async interface for Source RCON protocol | 💤 | 2020-08-26 | - | 25 |
| [aio_api_ros](https://github.com/frostspb/aio_api_ros) | Async Mikrotik API client | 💤 | 2023-03-02 | 0.0.19 | 25 |
| [aiobfd](https://github.com/netedgeplus/aiobfd) | Bidirectional Forwarding Detection (BFD) daemon for asyncio | 💤 | 2017-10-13 | 0.2 | 22 |
| [aioppspp](https://github.com/aio-libs/aioppspp) | Peer-to-Peer Streaming Protocol (PPSP) implementation | 💤 | 2016-02-03 | - | 20 |
| [aioxmpp](https://github.com/horazont/aioxmpp) | XMPP library for asyncio clients and servers | 🗄️ | 2024-01-14 | 0.13.3 | 216 |
| [aioshadowsocks](https://github.com/Ehco1996/aioshadowsocks) | Shadowsocks proxy implementation using asyncio | 🗄️ | 2021-06-27 | 0.1.8 | 165 |
| [aiosnmp](https://github.com/hh-h/aiosnmp) | Async SNMP client and trap server for asyncio | 🗄️ | 2026-07-12 | 0.7.2 | 54 |
| [AsyncIRC](https://github.com/kageurufu/AsyncIRC) | Buffered non-blocking IRC client library | 🗄️ | 2016-04-13 | 0.0.3 | 35 |
| [aiosocksy](https://github.com/romis2012/aiosocksy) | SOCKS proxy client for aiohttp | 🗄️ | 2018-08-29 | 0.1.2 | 32 |

### Cloud and DevOps

SDKs and clients for cloud providers, Kubernetes and Docker.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [aiobotocore](https://github.com/aio-libs/aiobotocore) | Asyncio support for botocore library using aiohttp for AWS API access | ✅ | 2026-10-02 | 3.9.2 | 1.4k |
| [aioboto3](https://github.com/terricain/aioboto3) | Wrapper to use boto3 resources with the aiobotocore async backend | ✅ | 2025-10-30 | 15.5.0 | 1.0k |
| [aiodocker](https://github.com/aio-libs/aiodocker) | Python Docker API client based on asyncio and aiohttp | ✅ | 2026-06-04 | 0.27.0 | 538 |
| [aiograpi](https://github.com/subzeroid/aiograpi) | Asynchronous client library for Instagram Private API | ✅ | 2026-10-04 | 2.0.15 | 460 |
| [kubernetes_asyncio](https://github.com/tomplus/kubernetes_asyncio) | Asynchronous client library for Kubernetes | ✅ | 2026-09-11 | 36.1.0 | 437 |
| [aiogoogle](https://github.com/omarryhan/aiogoogle) | Asynchronous client library for Google API and authentication | ✅ | 2026-07-18 | 5.19.0 | 224 |
| [aioaws](https://github.com/samuelcolvin/aioaws) | Asyncio compatible SDK for AWS services | 💤 | 2024-08-16 | 0.15.1 | 180 |
| [aiomql](https://github.com/Ichinga-Samuel/aiomql) | Async client library for MetaTrader 5 trading platform | ✅ | 2026-02-28 | 4.1.2 | 150 |
| [aiops-modules](https://github.com/awslabs/aiops-modules) | Reusable IaC modules for ML and GenAI on AWS | ✅ | 2026-03-18 | v3.2.6 | 104 |
| [aiomoex](https://github.com/WLM1ke/aiomoex) | Async client for Moscow Stock Exchange ISS API | 💤 | 2025-05-25 | 2.2.0 | 104 |
| [aiovk](https://github.com/alexanderlarin/aiovk) | Async client library for VKontakte (VK.com) API | 💤 | 2023-04-10 | 4.1.0 | 97 |
| [aiosnow](https://github.com/rbw/aiosnow) | Asynchronous client library for ServiceNow API | 💤 | 2021-01-24 | 0.6.0 | 73 |
| [async_dropbox](https://github.com/bdarnell/async_dropbox) | Async client for Dropbox API | 💤 | 2013-05-23 | - | 71 |
| [aiosend](https://github.com/vovchic17/aiosend) | Asynchronous client for Crypto Pay API | ✅ | 2026-09-18 | 3.0.8.post1 | 60 |
| [aioqzone](https://github.com/aioqzone/aioqzone) | Async client library for Qzone social network API | ✅ | 2026-08-15 | 1.9.9.dev1 | 54 |
| [aiozk](https://github.com/micro-fan/aiozk) | Async client for Apache ZooKeeper | 💤 | 2025-08-07 | 0.32.0 | 51 |
| [aiopokeapi](https://github.com/beastmatser/aiopokeapi) | Asynchronous wrapper for Pokemon API | ✅ | 2026-04-08 | 0.1.13 | 51 |
| [async-firebase](https://github.com/healthjoy/async-firebase) | Lightweight async client for Firebase Cloud Messaging | ✅ | 2026-10-04 | 6.3.0 | 48 |
| [aiopvpc](https://github.com/azogue/aiopvpc) | Library for fetching Spanish electricity hourly prices from PVPC API | 💤 | 2024-03-25 | 4.3.1 | 47 |
| [AIonDemandCluster](https://github.com/jhammant/AIonDemandCluster) | GPU cluster manager with Claude Code integration | ✅ | 2026-09-20 | 0.5.0 | 42 |
| [AsyncPayments](https://github.com/I-ToSa-I/AsyncPayments) | Async payment processing library | ✅ | 2026-08-31 | 1.7 | 40 |
| [aiofcm](https://github.com/Fatal1ty/aiofcm) | Firebase Cloud Messaging (FCM) client for asyncio | 💤 | 2023-04-16 | 1.4 | 35 |
| [aioambient](https://github.com/bachya/aioambient) | Asynchronous client for Ambient Weather API | 💤 | 2025-02-04 | 2025.2.0 | 35 |
| [async_yookassa](https://github.com/proDreams/async_yookassa) | Asynchronous client library for YooKassa payment API | ✅ | 2026-07-20 | 1.0.3 | 34 |
| [aiohttp-s3-client](https://github.com/aiokitchen/aiohttp-s3-client) | Async AWS S3 client for aiohttp | ✅ | 2026-02-12 | 1.1.2 | 33 |
| [aiotiktok](https://github.com/sheldygg/aiotiktok) | Asynchronous client library for TikTok API | 💤 | 2024-07-21 | 3.0.0 | 31 |
| [aiomixcloud](https://github.com/amikrop/aiomixcloud) | Async client library for Mixcloud API | 💤 | 2024-02-27 | 1.0.6 | 31 |
| [aiogcd](https://github.com/cesbit/aiogcd) | Async Google Cloud Datastore client | ✅ | 2026-03-25 | 1.0.2 | 29 |
| [aio-eth](https://github.com/Narasimha1997/aio-eth) | Async library for Ethereum blockchain Web3 JSON-RPC queries | 💤 | 2022-04-24 | 0.0.1 | 28 |
| [async-titiler](https://github.com/developmentseed/async-titiler) | Asynchronous GeoTIFF tile server based on TiTiler | ✅ | 2026-10-01 | - | 27 |
| [aiowiki](https://github.com/Gelbpunkt/aiowiki) | Asynchronous client for MediaWiki API | 💤 | 2021-02-21 | 0.2.0 | 24 |
| [aiokubernetes](https://github.com/olitheolix/aiokubernetes) | Async Kubernetes client library | 💤 | 2018-10-22 | 0.6 | 24 |
| [async-kinesis](https://github.com/hampsterx/async-kinesis) | Async client for AWS Kinesis | ✅ | 2026-05-06 | 2.5.6 | 24 |
| [aiosu](https://github.com/NiceAesth/aiosu) | Async client library for osu! game API | ✅ | 2026-09-22 | 2.5.1 | 23 |
| [aiotfm](https://github.com/Athesdrake/aiotfm) | Asynchronous event-based client for Transformice game | 💤 | 2024-09-22 | 1.4.9 | 22 |
| [aiobastion](https://github.com/safepost/aiobastion) | Framework for Cyberark API | 💤 | 2025-06-04 | v0.1.9 | 22 |
| [aiotx](https://github.com/crypto-libs/aiotx) | Asynchronous blockchain transaction monitoring and sending | 💤 | 2025-10-01 | 10.0.0 | 22 |
| [aiooss2](https://github.com/karajan1001/aiooss2) | Async client for Aliyun OSS (Object Storage Service) | 💤 | 2024-05-06 | 0.2.11 | 21 |
| [aiokalshi](https://github.com/the-odds-company/aiokalshi) | Async client for Kalshi prediction market API | ✅ | 2025-10-09 | - | 20 |
| [async-oss](https://github.com/Yaocool/async-oss) | Async SDK for Aliyun Object Storage Service (OSS) | 💤 | 2024-07-05 | - | 20 |
| [aioedgeos](https://github.com/brontide/aioedgeos) | Asynchronous API client for EdgeOS device management | 🗄️ | 2020-07-21 | - | 38 |

### Files and I/O

Async file access, subprocesses, serial ports and streams.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [aiofiles](https://github.com/Tinche/aiofiles) | File support for asyncio | ✅ | 2026-09-28 | 25.1.0 | 3.3k |
| [aiofile](https://github.com/mosquito/aiofile) | Real asynchronous file operations with native support | ✅ | 2026-08-23 | 3.12.3 | 584 |
| [aiopath](https://github.com/alexdelorenzo/aiopath) | Asynchronous pathlib for asyncio | 💤 | 2024-10-20 | 0.7.7 | 197 |
| [aionotify](https://github.com/rbarrois/aionotify) | Asyncio wrapper for Linux inotify file system events | 💤 | 2024-05-15 | 0.3.1 | 125 |
| [aiocogeo](https://github.com/geospatial-jeff/aiocogeo) | Async reader for Cloud Optimized GeoTIFF files | 💤 | 2021-01-03 | 0.3.0 | 76 |
| [aiocsv](https://github.com/MKuranowski/aiocsv) | Asynchronous CSV reading and writing | ✅ | 2026-05-23 | 1.4.1 | 74 |
| [async-pmtiles](https://github.com/developmentseed/async-pmtiles) | Async PMTiles reader for Python | ✅ | 2026-09-14 | 0.1.0 | 58 |
| [async-geotiff](https://github.com/developmentseed/async-geotiff) | Async reader for GeoTIFF and Cloud Optimized GeoTIFF files | ✅ | 2026-09-29 | 0.5.1 | 58 |
| [aiodl](https://github.com/cshuaimin/aiodl) | Asynchronous download utility | 💤 | 2020-08-04 | 0.5.7 | 56 |
| [aioshutil](https://github.com/kumaraditya303/aioshutil) | Async equivalents of shutil functions | ✅ | 2026-08-23 | 1.6 | 50 |
| [asyncinotify](https://github.com/ProCern/asyncinotify) | Async inotify module for file system monitoring | ✅ | 2026-05-28 | 4.4.4 | 47 |
| [async-downloader](https://github.com/ShichaoMa/async-downloader) | Async downloader utility | 💤 | 2018-06-30 | 0.2.1 | 33 |
| [aiowinreg](https://github.com/skelsec/aiowinreg) | Registry hive parsing using asyncio | ✅ | 2025-10-29 | 0.0.13 | 24 |

### Concurrency utilities

Primitives, rate limiters, pools, timeouts and runners.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [asyncer](https://github.com/fastapi/asyncer) | Utility library for working with asyncio coroutines and async/await syntax | ✅ | 2026-09-02 | 0.0.18 | 2.5k |
| [aiomultiprocess](https://github.com/omnilib/aiomultiprocess) | Run asyncio code across multiple processes | 💤 | 2024-07-22 | 0.9.1 | 1.9k |
| [aiostream](https://github.com/vxgmichel/aiostream) | Generator-based operators for asynchronous iteration | ✅ | 2026-09-16 | 0.8.1 | 921 |
| [aiolimiter](https://github.com/mjpieters/aiolimiter) | Rate limiter implementation for asyncio tasks | ✅ | 2026-10-04 | 1.3.0 | 784 |
| [aioprocessing](https://github.com/dano/aioprocessing) | Integration of multiprocessing module with asyncio for parallel execution | 💤 | 2022-09-16 | 2.0.1 | 661 |
| [aiorun](https://github.com/cjrh/aiorun) | A run() function that handles all the usual boilerplate for startup and graceful shutdown | ✅ | 2026-08-20 | 2025.1.1 | 470 |
| [aiometer](https://github.com/florimondmanca/aiometer) | Concurrency scheduling library supporting asyncio and trio | 💤 | 2025-04-04 | 1.0.0 | 440 |
| [aiomisc](https://github.com/aiokitchen/aiomisc) | Miscellaneous utils for asyncio | ✅ | 2026-09-28 | 18.0.33 | 426 |
| [aioreactive](https://github.com/dbrattli/aioreactive) | Reactive programming utilities for async/await code | 💤 | 2025-09-11 | 0.20.0 | 401 |
| [aioredlock](https://github.com/joanvila/aioredlock) | Distributed locking for asyncio using Redis | 💤 | 2022-05-19 | 0.7.3 | 317 |
| [aioitertools](https://github.com/omnilib/aioitertools) | Async-compatible itertools and builtins for asyncio | ✅ | 2025-11-06 | 0.13.0 | 278 |
| [aiochan](https://github.com/zh217/aiochan) | CSP-style concurrency with channels, select and multiprocessing on top of asyncio | 💤 | 2022-11-29 | 0.2.7 | 184 |
| [aiorwlock](https://github.com/aio-libs/aiorwlock) | Read write lock for asyncio | ✅ | 2026-10-04 | 1.5.1 | 176 |
| [aiosignal](https://github.com/aio-libs/aiosignal) | List of registered asynchronous callbacks for event handling | ✅ | 2026-09-30 | 1.4.0 | 170 |
| [aiotools](https://github.com/achimnol/aiotools) | Idiomatic asyncio utilities and helpers | ✅ | 2026-07-21 | 2.2.4 | 168 |
| [asyncio-throttle](https://github.com/hallazzang/asyncio-throttle) | Simple rate limiter for asyncio applications | 💤 | 2021-04-07 | 1.0.2 | 128 |
| [asyncio-pool](https://github.com/gistart/asyncio-pool) | Worker pool for asyncio with multiprocessing and threading support | 💤 | 2022-05-21 | 0.6.0 | 120 |
| [asyncio-buffered-pipeline](https://github.com/michalc/asyncio-buffered-pipeline) | Utility for parallelizing asyncio iterator pipelines | 💤 | 2020-11-09 | 0.0.8 | 118 |
| [async_generator](https://github.com/python-trio/async_generator) | Backward compatibility for async generators from Python 3.5 | 💤 | 2018-08-01 | 1.10 | 104 |
| [async_property](https://github.com/ryananguiano/async_property) | Python decorator for async properties | 💤 | 2023-09-05 | 0.2.2 | 98 |
| [aiologic](https://github.com/x42005e1f/aiologic) | GIL-powered locking library for asyncio | ✅ | 2026-09-26 | 0.17.1 | 93 |
| [asyncpool](https://github.com/CaliDog/asyncpool) | Coroutine worker pool for managing concurrent asyncio tasks | 💤 | 2018-01-24 | 1.0 | 79 |
| [asyncio_extras](https://github.com/agronholm/asyncio_extras) | Async generators, context managers and utilities for asyncio | 💤 | 2018-06-04 | 1.3.2 | 63 |
| [aioinject](https://github.com/notypecheck/aioinject) | Async-first dependency injection library for Python | ✅ | 2026-07-23 | 1.11.0 | 60 |
| [asyncio-redis-rate-limit](https://github.com/wemake-services/asyncio-redis-rate-limit) | Rate limiting utility using Redis backend for asyncio | ✅ | 2026-10-02 | 1.1.0 | 54 |
| [asyncpal](https://github.com/pyrustic/asyncpal) | Concurrency and parallelism utilities for asyncio | 💤 | 2024-12-02 | 0.0.7 | 46 |
| [aiochannel](https://github.com/tudborg/aiochannel) | Closable queues (channels) for Python asyncio | ✅ | 2026-08-03 | 1.4.1 | 41 |
| [asynciolimiter](https://github.com/bharel/asynciolimiter) | Rate limiter for asyncio applications | 💤 | 2025-08-01 | 1.2.0 | 39 |
| [AioContext](https://github.com/sqreen/AioContext) | Context storage and management for asyncio applications | 💤 | 2019-11-17 | 0.1.1 | 37 |
| [async-utils](https://github.com/mikeshardmind/async-utils) | Collection of async utilities | ✅ | 2026-09-20 | - | 34 |
| [aiobreaker](https://github.com/arlyon/aiobreaker) | Circuit breaker pattern implementation for asyncio | 💤 | 2021-12-27 | 1.2.0 | 30 |
| [aioraft](https://github.com/lisael/aioraft) | RAFT consensus algorithm implementation for asyncio | 💤 | 2015-08-09 | 0.1a0 | 29 |
| [asyncio-connection-pool](https://github.com/fellowapp/asyncio-connection-pool) | High-throughput connection pool implementation for asyncio | 💤 | 2025-03-07 | 1.1.1 | 28 |
| [async-caches](https://github.com/rafalp/async-caches) | Async caching library with multiple backends | 💤 | 2021-06-13 | 0.3.0 | 28 |
| [aio-executor](https://github.com/miguelgrinberg/aio-executor) | Executor implementation for running asyncio tasks in an event loop | 💤 | 2020-11-21 | 0.2.0 | 23 |
| [aioscript](https://github.com/asvetlov/aioscript) | Async operations abstraction with threading and multiprocessing support | 💤 | 2018-02-02 | - | 22 |
| [async_retrying](https://github.com/hellysmile/async_retrying) | Retry mechanism with backoff strategies for asyncio functions | 💤 | 2017-11-21 | - | 22 |
| [async-reduce](https://github.com/sirkonst/async-reduce) | Reducer utility for coordinating concurrent coroutines | 💤 | 2025-01-18 | 1.4 | 21 |
| [asyncio-multisubscriber-queue](https://github.com/smithk86/asyncio-multisubscriber-queue) | Queue for single producer to multiple consumers | 💤 | 2022-12-02 | 0.4.1 | 21 |
| [async-timeout](https://github.com/aio-libs-abandoned/async-timeout) | Asyncio-compatible timeout context manager | 🗄️ | 2025-09-22 | v5.0.1 | 570 |
| [aiotask-context](https://github.com/Skyscanner/aiotask-context) | Context management utilities for asyncio tasks | 🗄️ | 2020-01-21 | - | 159 |
| [aiodine](https://github.com/bocadilloproject/aiodine) | Async-first Python dependency injection library | 🗄️ | 2019-10-15 | 1.2.9 | 53 |
| [aiopipe](https://github.com/kchmck/aiopipe) | Multiprocess communication pipes for asyncio | 🗄️ | 2020-12-20 | 0.2.2 | 32 |
| [aioredis-lock](https://github.com/mattrasband/aioredis-lock) | Distributed locking implementation for aioredis | 🗄️ | 2019-12-10 | v0.1.0 | 24 |

### Event loops

Alternative event loop implementations.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [uvloop](https://github.com/MagicStack/uvloop) | Drop-in replacement for the asyncio event loop, built on libuv | ✅ | 2026-10-01 | 0.23.0 | 11.9k |
| [winloop](https://github.com/Vizonex/Winloop) | Alternative library for uvloop compatibility with Windows | ✅ | 2026-10-02 | 0.7.0 | 232 |
| [aiouv](https://github.com/saghul/aiouv) | Event loop implementation compatible with PEP-3156 asyncio specification | 💤 | 2015-08-12 | 0.0.1 | 69 |
| [asyncio-glib](https://github.com/jhenstridge/asyncio-glib) | Python asyncio event loop implementation on top of GLib | 💤 | 2019-09-05 | 0.1 | 36 |
| [pyuv](https://github.com/saghul/pyuv) | Python interface for libuv event loop implementation | 🗄️ | 2020-02-12 | 1.4.0 | 1.1k |

### Testing

Test runners, mocks and fixtures for async code.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) | Pytest support for asyncio | ✅ | 2026-10-01 | 1.4.0 | 1.7k |
| [respx](https://github.com/lundberg/respx) | Mock HTTPX library with awesome patterns and side effects for testing async code | ✅ | 2026-04-23 | 0.23.1 | 839 |
| [aioresponses](https://github.com/pnuckowski/aioresponses) | Helper for mock/fake web requests in Python aiohttp package | ✅ | 2026-04-13 | 0.7.9 | 556 |
| [asynctest](https://github.com/Martiusweb/asynctest) | Enhance the standard unittest package with features for testing. asyncio libraries | 💤 | 2019-11-13 | 0.13.0 | 310 |
| [async-asgi-testclient](https://github.com/vinissimus/async-asgi-testclient) | Framework-agnostic test client for ASGI applications | 💤 | 2022-06-13 | 1.4.11 | 161 |
| [aresponses](https://github.com/aresponses/aresponses) | Asyncio http mocking. Similar to the responses library used for requests | 💤 | 2024-07-11 | 3.0.0 | 106 |
| [aiogram_tests](https://github.com/OCCASS/aiogram_tests) | Test utilities and fixtures for aiogram bot framework | 💤 | 2023-02-20 | v1.0.3 | 71 |
| [aiounittest](https://github.com/kwarunek/aiounittest) | Test framework for Python asyncio code | ✅ | 2026-01-19 | 1.5.0 | 58 |
| [asyncpg-stubs](https://github.com/bryanforbes/asyncpg-stubs) | Type stubs for the asyncpg PostgreSQL driver | ✅ | 2026-07-10 | 0.31.3 | 50 |
| [asyncinject](https://github.com/simonw/asyncinject) | Async workflow execution with pytest-style dependency injection | ✅ | 2026-06-11 | 0.7 | 37 |
| [aiomock](https://github.com/nhumrich/aiomock) | A python mock library that supports async methods | 💤 | 2024-04-19 | 0.1.0 | 28 |
| [asyncio-testing](https://github.com/miguelgrinberg/asyncio-testing) | Helpers for unit testing asyncio code | 💤 | 2017-02-08 | - | 27 |
| [async_factory_boy](https://github.com/kuzxnia/async_factory_boy) | Factory Boy integration for async ORM testing | 💤 | 2023-08-12 | 1.0.1 | 25 |

### Observability and debugging

Tracing, metrics, profiling and debugging tools.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [opentelemetry-api](https://github.com/open-telemetry/opentelemetry-python) | OpenTelemetry Python API for distributed tracing and metrics collection | ✅ | 2026-10-01 | 1.45.0 | 2.7k |
| [aiomonitor](https://github.com/aio-libs/aiomonitor) | Monitor and REPL for asyncio applications | ✅ | 2026-03-30 | 0.7.1 | 777 |
| [aiozipkin](https://github.com/aio-libs/aiozipkin) | Distributed tracing instrumentation for asyncio with zipkin | 💤 | 2025-01-02 | 1.1.1 | 193 |
| [aioprometheus](https://github.com/claws/aioprometheus) | Prometheus metrics client library for asyncio applications | 💤 | 2023-12-27 | 23.12.0 | 189 |
| [aiologger](https://github.com/async-worker/aiologger) | Asynchronous logging handler for asyncio applications | 💤 | 2023-06-13 | 0.7.0 | 152 |
| [aiodebug](https://github.com/qntln/aiodebug) | A tiny library for monitoring and testing asyncio programs | 💤 | 2022-01-04 | 2.3.0 | 65 |
| [aiologstash](https://github.com/aio-libs/aiologstash) | Asyncio logging handler for Logstash integration | 💤 | 2022-01-23 | 2.0.0 | 57 |
| [aiohttp-sentry](https://github.com/underyx/aiohttp-sentry) | Sentry error reporting middleware for aiohttp | 💤 | 2021-06-30 | 0.6.0 | 35 |
| [aiodogstatsd](https://github.com/Gr1N/aiodogstatsd) | Async StatsD client with DogStatsD extension | 💤 | 2021-12-12 | 0.16.0.post0 | 34 |
| [aiomanhole](https://github.com/nhoad/aiomanhole) | Manhole for accessing asyncio applications | 💤 | 2022-01-23 | - | 31 |
| [aio-monitor](https://github.com/Physton/aio-monitor) | Real-time system monitoring panel for multiple platforms | 💤 | 2024-05-21 | v0.0.5 | 28 |
| [aiocop](https://github.com/Feverup/aiocop) | Monitor asyncio event loop for blocking I/O and CPU calls | ✅ | 2026-08-24 | 1.2.0 | 21 |

### Scraping and browser automation

Crawlers and headless browser drivers.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [Crawlee](https://github.com/apify/crawlee-python) | Web scraping and automation library for crawlers, extracts data with proxy rotation | ✅ | 2026-10-02 | 1.10.3 | 9.6k |
| [ruia](https://github.com/howie6879/ruia) | An async web scraping micro-framework based on asyncio | 💤 | 2022-08-21 | 0.8.5 | 1.7k |
| [async-proxy-pool](https://github.com/chenjiandongx/async-proxy-pool) | Asynchronous proxy pool for web scraping | 💤 | 2019-03-14 | - | 366 |
| [aioscpy](https://github.com/ihandmine/aioscpy) | Async web scraper imitating scrapy patterns | 💤 | 2025-04-18 | 0.3.13 | 115 |
| [asyncpy](https://github.com/lixi5338619/asyncpy) | Lightweight async web scraping framework | 💤 | 2022-10-23 | 1.2.0 | 103 |
| [aiocfscrape](https://github.com/pavlodvornikov/aiocfscrape) | Async module to bypass Cloudflare anti-bot protection | 💤 | 2020-03-25 | 1.0.0 | 80 |
| [aio-scrapy](https://github.com/ConlinH/aio-scrapy) | Web scraper implementing scrapy patterns with asyncio | ✅ | 2026-07-23 | 2.1.9 | 71 |
| [aiohttp_chromium](https://github.com/milahu/aiohttp_chromium) | Aiohttp-like interface to Chromium | ✅ | 2025-12-01 | - | 62 |
| [aio-vextractor](https://github.com/panoslin/aio-vextractor) | Video information parser for multiple platforms | 💤 | 2023-03-10 | - | 60 |
| [async-spider](https://github.com/waahah/async-spider) | Async web scraper for downloading content | 💤 | 2023-07-23 | - | 60 |
| [async-pubmed-scraper](https://github.com/IliaZenkov/async-pubmed-scraper) | Async scraper for PubMed article search and extraction | 💤 | 2020-11-05 | - | 45 |
| [aioScrapy](https://github.com/bytebuff/aioScrapy) | Async web scraper framework based on asyncio | 💤 | 2019-10-25 | - | 35 |
| [aiopytesseract](https://github.com/amenezes/aiopytesseract) | Async wrapper for Tesseract OCR text extraction | ✅ | 2026-01-14 | 1.1.0 | 28 |
| [async-bili-spider](https://github.com/chenjiandongx/async-bili-spider) | Async web scraper for Bilibili video platform | 💤 | 2019-02-16 | - | 24 |
| [aiohttp-spider](https://github.com/Crypto-KK/aiohttp-spider) | Async web scraper with aiohttp | 💤 | 2019-03-05 | - | 22 |
| [aiochrome](https://github.com/fate0/aiochrome) | Async client for Chrome DevTools Protocol | 💤 | 2017-09-28 | 0.0.3 | 22 |

### Bots and chat

Client libraries for chat platforms and bot frameworks.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) | Fully asynchronous Python interface for Telegram Bot API with type hints | ✅ | 2026-10-01 | 22.8 | 29.5k |
| [discord.py](https://github.com/Rapptz/discord.py) | Async API wrapper for Discord | ✅ | 2026-09-01 | 2.7.1 | 16.2k |
| [nonebot2](https://github.com/nonebot/nonebot2) | Cross-platform asynchronous chatbot framework supporting multiple backends | ✅ | 2026-09-28 | 2.5.0 | 7.7k |
| [aiogram](https://github.com/aiogram/aiogram) | Modern asynchronous framework for Telegram Bot API | ✅ | 2026-09-27 | 3.31.0 | 5.9k |
| [aiogram_dialog](https://github.com/Tishka17/aiogram_dialog) | GUI framework for Telegram bots built on aiogram | ✅ | 2026-06-15 | 2.6.0 | 900 |
| [aiotg](https://github.com/szastupov/aiotg) | Async client library for Telegram Bot API | ✅ | 2026-01-07 | 2.0.0 | 377 |
| [aiocqhttp](https://github.com/nonebot/aiocqhttp) | Async Python SDK for CQHTTP protocol | 💤 | 2023-06-11 | 1.4.4 | 299 |
| [aiogram_calendar](https://github.com/noXplode/aiogram_calendar) | Calendar widget for Telegram bots with aiogram | 💤 | 2024-12-15 | 0.6.0 | 191 |
| [aioapns](https://github.com/Fatal1ty/aioapns) | Async client library for Apple Push Notification service | 💤 | 2025-04-14 | 4.0 | 165 |
| [aiocryptopay](https://github.com/layerqa/aiocryptopay) | Asynchronous client for Telegram Crypto Pay API | 💤 | 2025-07-04 | 0.4.8 | 103 |
| [aioalice](https://github.com/mahenzon/aioalice) | Async library for Yandex Dialogs API | 💤 | 2023-02-23 | 1.5.1 | 91 |
| [aiograph](https://github.com/aiogram/aiograph) | Async Telegra.ph API wrapper | 💤 | 2021-11-20 | 0.2 | 65 |
| [aiogram-media-group](https://github.com/deptyped/aiogram-media-group) | Handler for Telegram media groups and albums | 💤 | 2023-12-15 | 0.5.1 | 51 |
| [aiogram-tonconnect](https://github.com/nessshon/aiogram-tonconnect) | TON Connect UI integration library for aiogram Telegram bots | 💤 | 2025-06-06 | 0.15.0 | 49 |
| [AsyncLine](https://github.com/Alnyz/AsyncLine) | Async client library for LINE Bot Messaging API | 💤 | 2023-07-10 | v1.5.9.2 | 35 |
| [aiogram-forms](https://github.com/13g10n/aiogram-forms) | Form handling extension for aiogram | 💤 | 2023-08-06 | 1.1.1 | 28 |
| [aiogram_broadcaster](https://github.com/loRes228/aiogram_broadcaster) | Telegram message broadcaster library for aiogram bots | ✅ | 2025-10-17 | 0.6.8 | 25 |
| [aiogram_widgets](https://github.com/ggindinson/aiogram_widgets) | Pre-built UI widgets for aiogram Telegram bot framework | 💤 | 2023-12-14 | 1.2.7 | 24 |
| [asynctwitch](https://github.com/Martmists-GH/asynctwitch) | Asynchronous Twitch chat client | 💤 | 2017-08-12 | - | 24 |
| [aiogram-inline-paginations](https://github.com/daniilshamraev/aiogram-inline-paginations) | Library for Telegram inline keyboard pagination | ✅ | 2025-11-05 | 0.1.12 | 23 |
| [aionostr](https://github.com/davestgermain/aionostr) | Async Nostr protocol client | 💤 | 2024-06-05 | 0.20.0 | 21 |
| [pyrogram](https://github.com/pyrogram/pyrogram) | Async Telegram MTProto API framework for users and bots | 🗄️ | 2024-12-23 | 2.0.106 | 4.6k |
| [aiotdlib](https://github.com/pylakey/aiotdlib) | Asynchronous Telegram client library based on TDLib | 🗄️ | 2026-01-16 | 0.27.6 | 146 |
| [aiomax](https://github.com/dpnspn/aiomax) | Asynchronous framework for Max Bot API | 🗄️ | 2026-07-14 | 2.12.5 | 42 |

### Auth and security

Authentication, authorization and crypto helpers.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [authlib](https://github.com/authlib/authlib) | Ultimate Python library for building OAuth and OpenID Connect servers and clients | ✅ | 2026-08-31 | 1.8.0 | 5.4k |
| [aiohttp-security](https://github.com/aio-libs/aiohttp-security) | Authentication and permissions for aiohttp | ✅ | 2026-10-01 | 0.5.0 | 240 |
| [aioauth](https://github.com/aliev/aioauth) | OAuth 2.0 server implementation for asyncio | ✅ | 2026-07-26 | 2.0.1 | 230 |
| [aioauth-client](https://github.com/klen/aioauth-client) | OAuth client library for aiohttp | 💤 | 2025-04-10 | 0.30.1 | 145 |
| [aiohttp-jwt](https://github.com/hzlmn/aiohttp-jwt) | JSON Web Token middleware for aiohttp | 💤 | 2020-05-07 | 0.6.1 | 78 |
| [aioauth-fastapi](https://github.com/aliev/aioauth-fastapi) | Integration of aioauth authentication with FastAPI framework | 💤 | 2024-08-18 | 0.1.2 | 41 |
| [aio-hcaptcha](https://github.com/RuslanUC/aio-hcaptcha) | Async wrapper for hCaptcha | 💤 | 2022-10-28 | - | 21 |
| [aiohttp-login](https://github.com/imbolc/aiohttp-login) | Registration and authorization for aiohttp apps | 🗄️ | 2018-02-23 | 1.4.0 | 51 |

### CLI and TUI

Command line and terminal UI libraries with async support.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [Textual](https://github.com/Textualize/textual) | Framework for building terminal and web UIs with an async Python API | ✅ | 2026-07-11 | 8.2.8 | 37.4k |
| [aioconsole](https://github.com/vxgmichel/aioconsole) | Asynchronous console I/O for asyncio applications | ✅ | 2026-05-23 | 0.8.2 | 484 |
| [async-tkinter-loop](https://github.com/insolor/async-tkinter-loop) | Async event loop integration for tkinter GUI applications | ✅ | 2026-10-01 | 0.10.4 | 94 |
| [aiocmd](https://github.com/KimiNewt/aiocmd) | Automatic CLI builder using asyncio and prompt-toolkit | 💤 | 2021-12-29 | 0.1.5 | 29 |

### IoT and hardware

Home automation, devices and embedded protocols.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [aioesphomeapi](https://github.com/esphome/aioesphomeapi) | Async Python client for ESPHome native API | ✅ | 2026-09-25 | 46.6.0 | 198 |
| [aiohomematic](https://github.com/SukramJ/aiohomematic) | Interface for asyncio interaction with HomeMatic devices | ✅ | 2026-10-03 | 2026.10.3 | 168 |
| [aioserial](https://github.com/johannjhang/aioserial.py) | A drop-in replacement of pySerial | 💤 | 2022-07-25 | 1.3.1 | 145 |
| [aioserial.py](https://github.com/johannjhang/aioserial.py) | Async wrapper for serial port communication | 💤 | 2022-07-25 | - | 145 |
| [aioblescan](https://github.com/frawau/aioblescan) | Scan and decode Bluetooth Low Energy advertising packets | 💤 | 2023-01-14 | 0.2.14 | 127 |
| [aiov2_ctl](https://github.com/hackergadgets/aiov2_ctl) | Control client for uConsole AIO v2 board | ✅ | 2026-03-03 | - | 126 |
| [aiocomfoconnect](https://github.com/michaelarnauts/aiocomfoconnect) | Zehnder ComfoConnect interface for home ventilation systems | ✅ | 2026-08-03 | 0.2.1 | 107 |
| [aiounifi](https://github.com/Kane610/aiounifi) | Library for communicating with Ubiquiti UniFi controllers | ✅ | 2026-10-01 | 97 | 90 |
| [asynckivy](https://github.com/asyncgui/asynckivy) | Async support library for Kivy framework | ✅ | 2026-09-29 | 0.12.0 | 90 |
| [aioshelly](https://github.com/home-assistant-libs/aioshelly) | Control Shelly smart home devices via asyncio | ✅ | 2026-10-04 | 13.34.1 | 82 |
| [aiohue](https://github.com/home-assistant-libs/aiohue) | Control Philips Hue devices using asyncio | ✅ | 2026-09-28 | 4.9.0 | 75 |
| [aio_energy_management](https://github.com/kotope/aio_energy_management) | Home Assistant integration for energy management | ✅ | 2026-09-27 | 1.2.1 | 75 |
| [aiohomekit](https://github.com/Jc2k/aiohomekit) | Asyncio support for HomeKit protocol | ✅ | 2026-08-14 | 4.0.1 | 72 |
| [async_upnp_client](https://github.com/StevenLooman/async_upnp_client) | Async client for UPnP (Universal Plug and Play) devices | ✅ | 2026-10-03 | 0.48.2 | 56 |
| [aioamazondevices](https://github.com/chemelli74/aioamazondevices) | Async library for controlling Amazon smart home devices | ✅ | 2026-10-04 | 16.3.1 | 55 |
| [aiowebostv](https://github.com/home-assistant-libs/aiowebostv) | Async library to control LG webOS-based TVs | ✅ | 2026-09-28 | 0.10.0 | 55 |
| [aiotuya](https://github.com/frawau/aiotuya) | Async library for LAN control of Tuya devices | 💤 | 2021-06-23 | 0.1.0b2 | 49 |
| [asyncvnc](https://github.com/barneygale/asyncvnc) | Asynchronous VNC client for Python | 💤 | 2023-02-26 | 1.3.0 | 44 |
| [aiorospy](https://github.com/locusrobotics/aiorospy) | Asyncio wrapper for ROS Python client | ✅ | 2026-09-24 | - | 43 |
| [asyncari](https://github.com/M-o-a-T/asyncari) | Asterisk telephony API wrapper for Trio and asyncio | 💤 | 2025-06-19 | 0.20.6 | 42 |
| [aiokef](https://github.com/basnijholt/aiokef) | Asyncio Python API for KEF speakers | 💤 | 2023-09-01 | 0.2.17 | 41 |
| [aiosc](https://github.com/artfwo/aiosc) | Lightweight Open Sound Control implementation | ✅ | 2026-07-11 | 0.3 | 40 |
| [aioswitcher](https://github.com/TomerFi/aioswitcher) | Control Switcher smart devices via asyncio | ✅ | 2026-10-04 | 6.3.0 | 39 |
| [aiowmi](https://github.com/cesbit/aiowmi) | Async Windows Management Instrumentation queries | ✅ | 2026-04-03 | 1.1.3 | 31 |
| [aiobmsble](https://github.com/patman15/aiobmsble) | Async library for querying BMS (battery management systems) via Bluetooth | ✅ | 2026-09-30 | 0.29.0 | 30 |
| [aioaquarea](https://github.com/cjaliaga/aioaquarea) | Control Panasonic Aquarea heat pump devices asynchronously | ✅ | 2026-05-07 | 1.0.7 | 30 |
| [aioharmony](https://github.com/Harmony-Libs/aioharmony) | Async library for controlling Logitech Harmony devices | ✅ | 2026-09-18 | 1.0.10 | 28 |
| [asyncpioneer](https://github.com/realthk/asyncpioneer) | Control Pioneer audio/video receivers asynchronously | 💤 | 2022-08-09 | - | 28 |
| [asyncio-for-robotics](https://github.com/2lian/asyncio-for-robotics) | Asyncio interface for ROS 2 and robotics systems | ✅ | 2026-09-16 | 1.5.0 | 28 |
| [aioasuswrt](https://github.com/kennedyshead/aioasuswrt) | Async client for ASUS router via SSH/telnet | ✅ | 2026-09-28 | 2.2.2 | 26 |
| [aiolifx](https://github.com/aiolifx/aiolifx) | Async library for controlling LIFX smart bulbs via LAN | ✅ | 2026-05-26 | 1.2.2 | 26 |
| [aio-intex-spa](https://github.com/mathieu-mp/aio-intex-spa) | Control Intex wifi-enabled spa devices asynchronously | ✅ | 2025-10-24 | 0.9.1 | 25 |
| [aioecowitt](https://github.com/home-assistant-libs/aioecowitt) | EcoWitt weather station protocol library for asyncio | ✅ | 2026-10-03 | 2026.6.0 | 23 |
| [aiopppp](https://github.com/devbis/aiopppp) | Tool for managing PPPP cameras | 💤 | 2025-10-02 | 0.2.3 | 23 |
| [aioesphomeserver](https://github.com/peterkeen/aioesphomeserver) | ESPHome native protocol server implementation in Python | ✅ | 2026-07-09 | - | 22 |
| [aiofranka](https://github.com/younghyopark/aiofranka) | Async library for controlling Franka robots | ✅ | 2026-10-03 | 0.6.1 | 21 |
| [aioruckus](https://github.com/ms264556/aioruckus) | Async client for Ruckus Unleashed WiFi controller | ✅ | 2026-09-14 | 0.49 | 20 |

### Alternatives to asyncio

Other async runtimes and compatibility layers.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [trio](https://github.com/python-trio/trio) | Pythonic async I/O for humans and snake people | ✅ | 2026-10-01 | 0.34.0 | 7.3k |
| [AnyIO](https://github.com/agronholm/anyio) | High level asynchronous concurrency and networking framework that works on top of either trio or asyncio | ✅ | 2026-10-04 | 4.15.1 | 2.5k |
| [trio-asyncio](https://github.com/python-trio/trio-asyncio) | re-implementation of the asyncio mainloop on top of Trio | ✅ | 2026-05-18 | 0.16.0 | 204 |
| [asyncio-gevent](https://github.com/gfmio/asyncio-gevent) | Asyncio and gevent interoperability | 💤 | 2025-07-14 | 0.2.5 | 83 |
| [asyncoro](https://github.com/pgiri/asyncoro) | Framework for asynchronous distributed concurrent network programming | 💤 | 2018-03-01 | 4.5.6 | 49 |
| [aioresult](https://github.com/arthur-tacca/aioresult) | Capture and retrieve results from Trio or anyio tasks | ✅ | 2026-08-24 | 1.3 | 20 |
| [curio](https://github.com/dabeaz/curio) | The coroutine concurrency library | 🗄️ | 2025-12-21 | 1.6 | 4.1k |

### Misc

Everything else.

| Library | Description | Status | Last commit | Latest version | Stars |
|---|---|:-:|---|---|--:|
| [watchfiles](https://github.com/samuelcolvin/watchfiles) | Async file system monitoring with a Rust backend | ✅ | 2026-09-21 | 1.3.0 | 2.5k |
| [aiocache](https://github.com/aio-libs/aiocache) | Cache manager for different backends | ✅ | 2026-06-28 | 0.12.3 | 1.4k |
| [async-lru](https://github.com/aio-libs/async-lru) | LRU cache implementation for asyncio functions | ✅ | 2026-09-30 | 2.3.0 | 954 |
| [aiotieba](https://github.com/lumina37/aiotieba) | Async client library for Baidu Tieba community platform | ✅ | 2026-10-02 | 4.8.0 | 688 |
| [aioquant](https://github.com/paulran/aioquant) | Event-driven framework for quantitative trading | 💤 | 2025-05-26 | - | 500 |
| [aiosmtplib](https://github.com/cole/aiosmtplib) | Async SMTP client library for sending emails over asyncio | ✅ | 2026-09-18 | 5.1.3 | 433 |
| [asyncstdlib](https://github.com/maxfischer2781/asyncstdlib) | Async equivalents of itertools and functools | ✅ | 2026-10-04 | 3.14.0 | 380 |
| [aiosmtpd](https://github.com/aio-libs/aiosmtpd) | SMTP server implementation based on asyncio | ✅ | 2026-10-01 | 1.4.6 | 372 |
| [aiodataloader](https://github.com/syrusakbary/aiodataloader) | DataLoader batch utility for asyncio applications | ✅ | 2025-11-29 | 0.4.3 | 296 |
| [aiohttp-devtools](https://github.com/aio-libs/aiohttp-devtools) | Development tools for aiohttp applications | ✅ | 2026-10-01 | 1.1.2 | 266 |
| [aiopandas](https://github.com/telekinesis-inc/aiopandas) | Async support for Pandas map, apply and transform operations | 💤 | 2025-06-12 | 0.0.3 | 133 |
| [asyncache](https://github.com/hephex/asyncache) | Wrapper for cachetools library to work with async functions | 💤 | 2023-12-22 | 0.3.1 | 109 |
| [async-cache](https://github.com/iamsinghrajat/async-cache) | Caching solution for asyncio applications | ✅ | 2026-05-28 | 2.0.3 | 107 |
| [aioify](https://github.com/perkfly/aioify) | Make functions async and awaitable | 💤 | 2022-04-04 | - | 99 |
| [AsyncFlow](https://github.com/AsyncFlow-Sim/AsyncFlow) | Simulator for async distributed systems | 💤 | 2025-09-18 | v0.1.1 | 81 |
| [aiocontextvars](https://github.com/fantix/aiocontextvars) | Asyncio support for contextvars backport | 💤 | 2019-04-08 | 0.2.2 | 56 |
| [aio-mc-rcon](https://github.com/Iapetus-11/aio-mc-rcon) | Asynchronous RCON client for Minecraft server administration | ✅ | 2026-09-18 | 3.5.0 | 53 |
| [aiosendspin](https://github.com/Sendspin/aiosendspin) | Async library implementing the Sendspin protocol | ✅ | 2026-10-02 | 9.1.1 | 51 |
| [asyncapi-python](https://github.com/dutradda/asyncapi-python) | Publish events from asyncapi specification | 💤 | 2020-12-01 | - | 46 |
| [async-btree](https://github.com/geronimo-iia/async-btree) | Asynchronous behavior tree implementation for Python | ✅ | 2026-09-06 | 3.0.1 | 45 |
| [async-agentic-tools](https://github.com/mikegc-aws/async-agentic-tools) | Background task execution framework for AI agents | ✅ | 2026-05-28 | - | 41 |
| [async-class](https://github.com/mosquito/async-class) | Async constructor support for Python classes | 💤 | 2021-10-03 | 0.5.0 | 38 |
| [aioyagmail](https://github.com/kootenpv/aioyagmail) | Async email sending with Gmail | 💤 | 2018-06-27 | 0.0.4 | 33 |
| [aioutils](https://github.com/observerss/aioutils) | Utility functions for asyncio development | 💤 | 2015-03-12 | 0.3.10 | 33 |
| [async-django-email](https://github.com/python019/async-django-email) | Async email support for Django | 💤 | 2022-10-13 | - | 33 |
| [aiodag](https://github.com/mitstake/aiodag) | Build and execute DAGs with asyncio | 💤 | 2021-09-23 | 0.4 | 28 |
| [asyncio-ipython-magic](https://github.com/Gr1N/asyncio-ipython-magic) | IPython magic command extension for running asyncio code | 💤 | 2017-02-14 | 0.0.3 | 28 |
| [Aios](https://github.com/harshitgavita-07/Aios) | AI orchestration framework for building digital coworkers | ✅ | 2026-07-26 | v2.0.0 | 26 |
| [aioreloader](https://github.com/and800/aioreloader) | Auto-reloader for asyncio applications | 💤 | 2020-11-11 | 0.4.0 | 26 |
| [async-signals](https://github.com/ddanier/async-signals) | Async version of Django signals | ✅ | 2026-08-22 | v0.4.1 | 25 |
| [asyncapi-python](https://github.com/G-USI/asyncapi-python) | CLI to generate Python code from AsyncAPI spec | ✅ | 2026-04-04 | 0.3.1 | 24 |
| [aioredux](https://github.com/kasbah/aioredux) | Redux-style state management for asyncio applications | 💤 | 2018-08-05 | - | 23 |
| [AsyncPP](https://github.com/PluralisResearch/AsyncPP) | Asynchronous pipeline parallel optimization | ✅ | 2026-02-02 | - | 23 |
| [async-graph-data-flow](https://github.com/civisanalytics/async-graph-data-flow) | Async functions for directed acyclic graphs | ✅ | 2026-04-21 | 2.0.0 | 22 |
| [asyncgpt](https://github.com/Just1z/asyncgpt) | Async framework for ChatGPT API integration | 💤 | 2023-03-05 | - | 22 |
| [asyncio-atexit](https://github.com/minrk/asyncio-atexit) | Exit handlers and cleanup utilities for asyncio applications | 💤 | 2025-01-07 | 1.0.1 | 22 |
| [async-ipython-magic](https://github.com/leriomaggio/async-ipython-magic) | Async IPython magic for notebook cells | 💤 | 2020-12-04 | - | 22 |
| [asyncio_dispatch](https://github.com/lenzenmi/asyncio_dispatch) | Event signalling for asyncio | 💤 | 2015-11-12 | 1.1.0 | 20 |
| [asyncqt](https://github.com/gmarull/asyncqt) | Integration of asyncio event loop with PyQt and PySide | 🗄️ | 2020-12-29 | 0.8.0 | 155 |

## How the data is collected

[`libraries.yml`](libraries.yml) holds the name, repository, PyPI package, group and description of each library. [`tools/update.py`](tools/update.py) reads it, asks the GitHub GraphQL API for archive state, stars and last commit, asks PyPI for the latest version (falling back to the latest GitHub release), and rewrites this file. The release date comes from PyPI or GitHub, not from the commit.

A GitHub Action runs the script every Monday and commits the result. If a lookup fails, the previous values are kept. The agent instructions for the weekly run are in [`CLAUDE.md`](CLAUDE.md).

To run it yourself:

```console
$ uv run tools/update.py
```

## Contributing

Missing a library? [Open an issue](../../issues/new?template=add-library.yml) or send a pull request that adds an entry to `libraries.yml`. Details are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0](LICENSE). The list started from [timofurrer/awesome-asyncio](https://github.com/timofurrer/awesome-asyncio), which is no longer maintained.
