# 📬 Email Service System Design

System Design Project – Scalable Email Platform

---

# Problem Statement

Design a scalable email system similar to Gmail that allows users to send, receive, and store emails.

---

# Functional Requirements

- Send email
- Receive email
- Store emails
- Retrieve inbox messages

---

# Non Functional Requirements

- High availability
- Low latency message delivery
- Large storage capacity
- Horizontal scalability

---

# Core Concepts

• Message Queues  
• Mail Delivery Workers  
• Distributed Storage  
• Inbox Indexing  

---

# High Level Architecture

User
 ↓
API Gateway
 ↓
Email Service
 ↓
Message Queue
 ↓
Delivery Workers
 ↓
Mailbox Storage
