# Project-Specific Rules

> **Global Instructions:** See AGENTS.md for the 3-layer architecture and operating principles that apply to all projects.

## This Project

**Project Name:** VideoMigrator.com Website  
**Version:** 1.0.0  
**Purpose:** SaaS platform for migrating videos from Vimeo to Bunny.net with cost calculator, customer onboarding, and dashboard

### Tech Stack

**WordPress Stack:**
- WordPress with Kadence Theme
- WS Form (calculator and signup forms)
- FluentMCP (MCP server for AI-powered WordPress management)
- FluentCommunity (community posts, announcements, support)
- FluentCRM (customer relationship management)
- FluentCart (e-commerce and checkout flows)
- Stripe (payment processing)

**Backend & Data:**
- Python migration backend (existing project integration)
- Airtable API (4-table relational architecture)
- WordPress REST API

### Airtable Architecture (4 Tables)

1. **Calculator Results** - Cost analysis submissions from calculator
   - Vimeo costs, predicted savings, contact info
   - Routes to: Both Calculator Results + Customers tables

2. **Customers** - Master customer records
   - Contact info, subscription status, lifetime value
   - Linked to: Migration Runs, Revenues & Refunds

3. **Migration Runs** - Individual migration job tracking
   - Video counts, dates, status, actual savings
   - Linked to: Customers table

4. **Revenues & Refunds** - Financial transaction records
   - Stripe payments, refunds, revenue tracking
   - Linked to: Customers table

### Key APIs & Integration Points

**FluentMCP Integration:**
- Natural language WordPress content management
- Form creation and modification
- Post/page updates via AI commands
- Community post management

**WordPress REST API:**
- Form submissions retrieval
- Custom post types
- User authentication and access control
- Dashboard data display

**Airtable API:**
- Dual-table form routing (Calculator → Calculator Results + Customers)
- Real-time stats updates from Python backend
- Customer dashboard data queries
- Revenue tracking and reporting

**Stripe API:**
- Checkout session creation
- Webhook handling for payment verification
- Subscription management
- Refund processing

### Data Flow Patterns

**Calculator Form Submission:**
1. User submits WS Form calculator
2. Form data → Airtable Calculator Results table (cost analysis)
3. Form data → Airtable Customers table (contact record)
4. Return: Predicted savings, migration estimate

**Customer Signup Flow:**
1. User chooses free trial or paid migration
2. Paid: Stripe checkout → FluentCart integration
3. Stripe webhook confirms payment
4. Create/update Customer record in Airtable
5. Grant dashboard access via WordPress

**Dashboard Display:**
1. WordPress authenticates customer
2. Query Airtable for customer's Migration Runs
3. Display: progress, predicted vs actual savings
4. Real-time updates from Python backend migration script

**Migration Stats Update:**
1. Python backend completes video migration
2. Update Airtable Migration Runs table
3. Webhook/polling triggers dashboard refresh
4. Customer sees updated progress

### Edge Cases to Handle

**Multi-Table Form Routing:**
- Single form submission must create records in TWO tables
- Calculator Results: Store cost analysis data
- Customers: Create/update master customer record
- Handle duplicate customer detection (email match)

**Authentication & Access Control:**
- Free trial vs paid migration permissions
- Dashboard access only for active customers
- Session management and security
- Role-based content restrictions

**Payment Flow Edge Cases:**
- Stripe checkout abandonment
- Webhook delivery failures
- Duplicate payment prevention
- Refund processing and customer status updates

**Real-Time Stats Updates:**
- Python backend may run for hours/days
- Handle connection timeouts gracefully
- Queue updates if Airtable API rate limited
- Display stale data warnings in dashboard

**API Rate Limiting:**
- Airtable: 5 requests/second
- WordPress REST API: Variable by hosting
- Stripe: 100 requests/second
- Implement sliding window rate limiter

### WordPress-Specific Considerations

**Theme:** Kadence Theme
- Custom dashboard page template
- Calculator page with WS Form embed
- Pricing comparison tables
- Customer testimonials section

**Forms (WS Form):**
- Cost calculator form (complex calculations)
- Signup/contact form
- Support ticket form in FluentCommunity

**Security:**
- API authentication for form submissions
- Dashboard data access control
- Stripe webhook signature verification
- Environment variables for all secrets

### Development Workflow

**Local Setup:**
1. WordPress local development environment
2. Python virtual environment for execution scripts
3. Airtable test base (separate from production)
4. Stripe test mode keys

**Testing:**
- Test form submissions with dummy data
- Verify dual-table routing in Airtable
- Test Stripe checkout flow (test mode)
- Validate dashboard displays correct data
- Test Python backend stats updates

**Deployment:**
- WordPress: Standard hosting deployment
- Python scripts: Server or cloud function deployment
- Environment variables via hosting control panel
- Webhook endpoints configured in Stripe/Airtable

### File Organization

**Directives (SOPs):**
- `setup_airtable_schema.md` - 4-table Airtable setup automation
- `calculator_form_integration.md` - WS Form → dual-table routing
- `customer_dashboard.md` - Dashboard display and data queries
- `stripe_checkout_flow.md` - Payment processing integration
- `migration_stats_update.md` - Python backend → Airtable updates
- `fluentcommunity_posts.md` - Community announcements and support

**Execution Scripts:**
- `setup_vimeobunny_airtable.py` - Automated 4-table schema creation
- `rate_limiter.py` - Intelligent API throttling (sliding window)
- `form_to_airtable.py` - Dual-table form routing handler
- `update_migration_stats.py` - Backend → Airtable sync
- `stripe_webhook_handler.py` - Payment verification
- `dashboard_data.py` - Customer dashboard queries

### Success Criteria

**Phase 1: Foundation**
- ✅ Airtable 4-table schema created and linked
- ✅ WordPress installed with Kadence Theme
- ✅ WS Form calculator configured
- ✅ FluentMCP integration tested

**Phase 2: Form Integration**
- ✅ Calculator form → dual-table Airtable routing
- ✅ Signup form → Customers table
- ✅ Form validation and error handling
- ✅ Email notifications configured

**Phase 3: Payment & Dashboard**
- ✅ Stripe checkout integration
- ✅ Webhook handling for payments
- ✅ Customer dashboard displays migration data
- ✅ Real-time stats updates from Python backend

**Phase 4: Community & Support**
- ✅ FluentCommunity announcements section
- ✅ Support ticket system
- ✅ Customer testimonials display
- ✅ Email drip campaigns via FluentCRM

### Notes for AI Agent

- **Always check for existing execution scripts before creating new ones**
- **Update directives as you learn about API limitations**
- **Test all Stripe integrations in test mode first**
- **Use FluentMCP for WordPress operations when possible (natural language)**
- **Implement rate limiting for all external API calls**
- **Handle form→multi-table routing carefully (data consistency)**
- **Security first: Never expose API keys, always use .env**
- **Document all Airtable formula fields and rollups in directives**

