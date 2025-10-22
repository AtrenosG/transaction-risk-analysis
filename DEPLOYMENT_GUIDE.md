# 🚀 Complete Railway Deployment Guide

## Transaction Risk Analytics API - Production Deployment

This guide provides step-by-step instructions to deploy your FastAPI backend to Railway with full production readiness.

---

## 📋 **Prerequisites**

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **GitHub Account**: For code repository
3. **Supabase Account**: For database (if using database features)
4. **Git**: Installed on your local machine

---

## 🛠️ **Step 1: Prepare Your Project**

### **1.1 Verify Project Structure**
Ensure your project has these files:
```
d:\MINI PROJECT\
├── app.py                      # ✅ Main FastAPI application
├── transaction_risk_model.py   # ✅ ML model
├── models/schemas.py           # ✅ Data models
├── routes/api.py              # ✅ API routes
├── services/                  # ✅ Services
├── utils/                     # ✅ Utilities
├── requirements.txt           # ✅ Dependencies
├── Dockerfile                 # ✅ Container config
├── Procfile                   # ✅ Railway process file
├── railway.json               # ✅ Railway config
├── .dockerignore             # ✅ Docker ignore
└── .env.example              # ✅ Environment template
```

### **1.2 Test Locally**
```bash
# Activate your virtual environment
& "d:/MINI PROJECT/minip/Scripts/Activate.ps1"

# Test the application
python app.py

# Verify endpoints work
curl http://localhost:8000/api/test
curl http://localhost:8000/api/health
```

---

## 🌐 **Step 2: Set Up GitHub Repository**

### **2.1 Initialize Git Repository**
```bash
cd "d:\MINI PROJECT"
git init
git add .
git commit -m "Initial commit: Transaction Risk Analytics API"
```

### **2.2 Create GitHub Repository**
1. Go to [github.com](https://github.com)
2. Click **"New repository"**
3. Name: `transaction-risk-analytics-api`
4. Description: `FastAPI backend for transaction risk scoring and financial behavior analytics`
5. Set to **Public** or **Private**
6. Click **"Create repository"**

### **2.3 Push to GitHub**
```bash
git remote add origin https://github.com/YOUR_USERNAME/transaction-risk-analytics-api.git
git branch -M main
git push -u origin main
```

---

## 🚂 **Step 3: Deploy to Railway**

### **3.1 Connect to Railway**
1. Go to [railway.app](https://railway.app)
2. Click **"Login"** and sign in with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your `transaction-risk-analytics-api` repository
6. Click **"Deploy Now"**

### **3.2 Configure Environment Variables**
In Railway dashboard:
1. Go to your project
2. Click **"Variables"** tab
3. Add these variables:

```bash
# Required Variables
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-supabase-anon-key

# Optional Variables
FRONTEND_URL=https://your-frontend-domain.vercel.app
WEBHOOK_URL=https://your-webhook-endpoint.com/webhook
DEBUG=false
```

### **3.3 Configure Railway Settings**
1. Go to **"Settings"** tab
2. **Build & Deploy**:
   - Build Command: `(leave empty - uses Dockerfile)`
   - Start Command: `(leave empty - uses Dockerfile CMD)`
3. **Networking**:
   - Enable **"Public Networking"**
   - Custom domain (optional): `your-api.railway.app`

---

## 🗄️ **Step 4: Set Up Supabase Database**

### **4.1 Create Supabase Project**
1. Go to [supabase.com](https://supabase.com)
2. Click **"New project"**
3. Choose organization and name: `transaction-risk-analytics`
4. Set database password (save it!)
5. Select region closest to your users
6. Click **"Create new project"**

### **4.2 Create Database Tables**
In Supabase SQL Editor, run:

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    account_no TEXT UNIQUE NOT NULL,
    ifsc_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Transactions table
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    date TIMESTAMP NOT NULL,
    description TEXT,
    amount DECIMAL(15,2) NOT NULL,
    type TEXT CHECK (type IN ('credit', 'debit')) NOT NULL,
    category TEXT,
    upi_app TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- ML Results table
CREATE TABLE ml_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    risk_score DECIMAL(5,2) NOT NULL,
    risk_category TEXT CHECK (risk_category IN ('low', 'medium', 'high')) NOT NULL,
    eligible BOOLEAN NOT NULL,
    eligibility_reason TEXT,
    metrics JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_date ON transactions(date);
CREATE INDEX idx_ml_results_user_id ON ml_results(user_id);
CREATE INDEX idx_ml_results_created_at ON ml_results(created_at);
```

### **4.3 Get Supabase Credentials**
1. Go to **"Settings"** → **"API"**
2. Copy **"Project URL"** → This is your `SUPABASE_URL`
3. Copy **"anon public"** key → This is your `SUPABASE_KEY`
4. Add these to Railway environment variables

---

## 🧪 **Step 5: Test Deployment**

### **5.1 Check Deployment Status**
1. In Railway dashboard, check **"Deployments"** tab
2. Wait for deployment to complete (green checkmark)
3. Click on the deployment to see logs

### **5.2 Test API Endpoints**
Your API will be available at: `https://your-project-name.up.railway.app`

```bash
# Test basic functionality
curl https://your-project-name.up.railway.app/api/test

# Test health check
curl https://your-project-name.up.railway.app/api/health

# Test API documentation
# Visit: https://your-project-name.up.railway.app/docs
```

### **5.3 Expected Responses**

**Test Endpoint** (`/api/test`):
```json
{
  "success": true,
  "data": {
    "message": "API is working",
    "timestamp": "2024-01-15T10:30:00.000000",
    "version": "1.0.0"
  },
  "message": "Test endpoint working successfully",
  "timestamp": "2024-01-15T10:30:00.000000"
}
```

**Health Check** (`/api/health`):
```json
{
  "success": true,
  "data": {
    "status": "healthy",
    "supabase": "connected",
    "ml_model": "ready",
    "supabase_status": true
  },
  "message": "Service is running with Supabase",
  "timestamp": "2024-01-15T10:30:00.000000"
}
```

---

## 📊 **Step 6: Test Full Functionality**

### **6.1 Add Sample Data**
In Supabase SQL Editor:

```sql
-- Insert sample user
INSERT INTO users (name, account_no, ifsc_code) 
VALUES ('John Doe', '1234567890', 'SBIN0001234');

-- Get user ID (replace with actual ID from above insert)
-- INSERT INTO transactions (user_id, date, description, amount, type, category, upi_app)
-- VALUES 
-- ('USER_ID_HERE', '2024-01-01', 'Salary Credit', 50000, 'credit', 'salary', null),
-- ('USER_ID_HERE', '2024-01-02', 'Grocery Shopping', 3000, 'debit', 'groceries', 'GPay'),
-- ('USER_ID_HERE', '2024-01-03', 'Electricity Bill', 1500, 'debit', 'utilities', 'PhonePe');
```

### **6.2 Test Analysis Endpoint**
```bash
curl "https://your-project-name.up.railway.app/api/analyze?account_no=1234567890&ifsc=SBIN0001234"
```

---

## 🔧 **Step 7: Production Optimizations**

### **7.1 Custom Domain (Optional)**
1. In Railway dashboard → **"Settings"** → **"Domains"**
2. Add custom domain: `api.yourdomain.com`
3. Update DNS records as instructed

### **7.2 Environment-Specific Configurations**
Add these Railway environment variables:

```bash
# Production optimizations
WORKERS=2
LOG_LEVEL=info
TIMEOUT=30

# Security
CORS_ORIGINS=https://yourfrontend.com,https://yourdomain.com

# Monitoring (optional)
SENTRY_DSN=your-sentry-dsn-here
```

### **7.3 Monitoring Setup**
1. Enable Railway metrics in dashboard
2. Set up alerts for deployment failures
3. Monitor API response times and error rates

---

## 🚨 **Troubleshooting**

### **Common Issues & Solutions**

**1. Deployment Fails**
```bash
# Check Railway logs
# Go to Railway dashboard → Deployments → Click on failed deployment
# Common causes:
# - Missing environment variables
# - Python dependency conflicts
# - Dockerfile issues
```

**2. Supabase Connection Issues**
```bash
# Verify credentials in Railway variables
# Test Supabase connection manually:
curl -X GET 'https://your-project-id.supabase.co/rest/v1/' \
  -H "apikey: your-supabase-anon-key"
```

**3. API Returns 500 Errors**
```bash
# Check Railway application logs
# Common causes:
# - Missing environment variables
# - Database connection issues
# - Code errors in ML model
```

**4. Health Check Fails**
```bash
# Test individual endpoints:
curl https://your-project-name.up.railway.app/api/test
curl https://your-project-name.up.railway.app/api/health
```

---

## 📈 **Step 8: Scaling & Maintenance**

### **8.1 Auto-Scaling**
Railway automatically scales based on traffic, but you can configure:
1. **Resource limits** in Railway dashboard
2. **Replica count** for high availability
3. **Health check intervals**

### **8.2 Updates & Deployments**
```bash
# To update your API:
git add .
git commit -m "Update: description of changes"
git push origin main

# Railway will automatically redeploy
```

### **8.3 Backup Strategy**
1. **Database**: Supabase handles automatic backups
2. **Code**: GitHub repository serves as backup
3. **Environment**: Document all environment variables

---

## ✅ **Deployment Checklist**

- [ ] ✅ Project structure verified
- [ ] ✅ Local testing completed
- [ ] ✅ GitHub repository created and pushed
- [ ] ✅ Railway project deployed
- [ ] ✅ Environment variables configured
- [ ] ✅ Supabase database set up
- [ ] ✅ Database tables created
- [ ] ✅ API endpoints tested
- [ ] ✅ Health checks passing
- [ ] ✅ Sample data tested
- [ ] ✅ Documentation accessible
- [ ] ✅ Monitoring configured

---

## 🎉 **Success!**

Your Transaction Risk Analytics API is now deployed and ready for production use!

**Your API URLs:**
- **Base URL**: `https://your-project-name.up.railway.app`
- **API Docs**: `https://your-project-name.up.railway.app/docs`
- **Health Check**: `https://your-project-name.up.railway.app/api/health`

**Next Steps:**
1. Integrate with your frontend application
2. Set up monitoring and alerts
3. Configure custom domain (optional)
4. Implement rate limiting (if needed)
5. Set up CI/CD pipeline for automated testing

---

## 📞 **Support**

If you encounter issues:
1. Check Railway deployment logs
2. Verify environment variables
3. Test Supabase connection
4. Review API documentation at `/docs`

**Happy Deploying! 🚀**
