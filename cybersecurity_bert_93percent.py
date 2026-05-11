import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import torch

# ============================================
# STEP 1: CREATE THE DATASET
# ============================================

data = {
    "text": [
        # Ransomware examples (label 0) - Add these 25 to your existing 15
        "Computer locked with message demanding payment in cryptocurrency",
        "All documents renamed with .locked extension, ransom note appeared",
        "Company servers encrypted overnight, hacker demands Bitcoin",
        "Files inaccessible, popup demands $5000 in Monero for decryption",
        "Network drives encrypted, ransom countdown timer showing 72 hours",
        "Employee received email with decryption key payment instructions",
        "Critical database files now have .ransom extension, backups also encrypted",
        "System rebooted to find all photos and documents encrypted",
        "Ransomware gang leaked sample data as proof of attack",
        "Production servers down, blackmail note demanding payment in crypto",
        "Accounting files renamed to .crypted, ransom note on desktop",
        "Hospital systems locked, attackers demand payment in Bitcoin",
        "Law firm client files encrypted, threat to publish sensitive data",
        "Backup servers compromised, shadow copies deleted automatically",
        "Ransom note claims files will double in price every 24 hours",
        "Decryption tool offered after payment to anonymous wallet address",
        "All PDF and Word documents now have .bozon extension, data unrecoverable",
        "Ransomware spread through remote desktop protocol compromise",
        "Encrypted files detected across multiple network shares simultaneously",
        "Ransom note threatens to sell stolen data on dark web forums",
        "Customer database encrypted, operations halted until payment made",
        "Windows event logs cleared after ransomware execution completed",
        "Files decrypted after paying ransom, but some data still corrupted",
        "Ransomware removed after payment, but backdoor remained installed",
        "Third-party decryption tool failed to recover encrypted files",

        # DDOS EXAMPLES (15 samples)
        # DDoS examples (label 1) - Add these 25 to your existing 15
        "E-commerce site inaccessible during peak shopping hours due to traffic flood",
        "Corporate website returns 504 gateway timeout every few minutes",
        "DNS server overwhelmed by 200,000 queries per second from botnet",
        "Online gaming platform experiencing 500ms latency due to packet flood",
        "API gateway reports 10,000 requests per second from single IP range",
        "Web application firewall blocking SYN packets from 150 countries",
        "Cloud load balancer scaling to maximum capacity during attack",
        "VoIP phone system unreachable due to SIP INVITE flood",
        "Mobile app users reporting login timeouts and connection drops",
        "NTP amplification attack generating 100Gbps of reflected traffic",
        "Memcached servers abused for 50x traffic amplification attack",
        "Slowloris attack holding thousands of connections open simultaneously",
        "HTTP GET flood overwhelming application server memory resources",
        "ICMP flood consuming all available network bandwidth",
        "DNS reflection attack using vulnerable DNS resolvers worldwide",
        "TCP SYN flood bypassing firewall due to distributed source IPs",
        "Application layer attack targeting search functionality with complex queries",
        "BGP route hijack redirecting traffic through malicious ASN",
        "WebSocket connection flood exhausting server file descriptors",
        "Redis server exploited for 100x amplification attack",
        "CHARGen protocol abused for UDP amplification attack",
        "SSDP reflection attack generating 30Gbps of garbage traffic",
        "RST flood causing connection resets on stateful firewalls",
        "HTTP slow post attack consuming web server threads for minutes",
        "XML-RPC attack using pingback method to amplify traffic 3000x",

        # Insider Threat examples (label 2) - Add these 25 to your existing 15
        "Employee attempted to bypass VPN restrictions using unauthorized software",
        "Terminated contractor still accessing systems using valid credentials",
        "Staff member copied proprietary source code to personal laptop",
        "Night shift employee accessed CEO's email folder without authorization",
        "Help desk employee reset passwords for accounts outside normal procedure",
        "Developer exported production database to personal cloud storage account",
        "Sales representative downloaded competitor analysis beyond job scope",
        "HR manager accessed medical records of non-direct report employees",
        "Intern emailed confidential design documents to personal address",
        "Employee installed unauthorized keylogger on work computer",
        "System administrator created hidden backdoor account for personal use",
        "Staff member shared MFA codes with external vendor bypassing policy",
        "Employee accessed systems from personal device during suspension period",
        "Former employee's badge still active 6 months after termination",
        "Contractor downloaded intellectual property day before contract end",
        "Employee searched for competitor job postings while accessing R&D files",
        "Night shift worker printed 500 pages of sensitive customer data",
        "Staff member disabled security software to install unapproved application",
        "Employee attempted to escalate privileges using known vulnerability",
        "Remote worker transferred files to unencrypted external hard drive",
        "Accounting staff accessed financial data of executive team members",
        "Employee photographed confidential documents using personal phone",
        "Staff member used colleague's credentials after shoulder surfing",
        "Disgruntled employee deleted critical configuration files before resignation",
        "Employee submitted fake help desk request to obtain admin password",

        # WEB ATTACK EXAMPLES (15 samples)
        # Web Attack examples (label 3) - Add these 25 to your existing 15
        "LDAP injection attempt bypassing authentication with malformed query",
        "Server-side request forgery attempting to access internal metadata endpoint",
        "XML external entity injection reading system files via file protocol",
        "HTTP header injection adding malicious response headers to cached pages",
        "Cross-site request forgery token missing in state-changing POST request",
        "Host header injection exploiting password reset functionality",
        "Content spoofing attack presenting fake login form on legitimate URL",
        "CSV injection payload in export feature to compromise analyst workstation",
        "Open redirect vulnerability exploited to send users to phishing site",
        "Remote file inclusion loading malicious PHP script from external server",
        "Local file disclosure reading /etc/passwd via path manipulation",
        "Unvalidated redirect used in OAuth callback parameter",
        "Server-side template injection attempting to execute system commands",
        "Expression language injection bypassing sandbox restrictions",
        "SQL boolean-based blind injection extracting data character by character",
        "Second-order SQL injection triggered after database write operation",
        "Out-of-band SQL injection using DNS exfiltration technique",
        "Command injection using backticks in user-supplied domain name",
        "Blind command injection with time-based detection via ping command",
        "XSS bypassing WAF using DOM-based JavaScript mutation technique",
        "Stored XSS in comment section executing when admin views page",
        "Reflected XSS in search parameter delivering cryptominer script",
        "DOM clobbering attack overriding JavaScript variables",
        "Prototype pollution affecting admin panel form validation",
        "GraphQL introspection query attempting to map entire API schema",

        # BENIGN EXAMPLES (15 samples)
        # Benign examples (label 4) - Add these 25 to your existing 15
        "Employee logged into company portal using single sign-on authentication",
        "IT department applied quarterly security patches to production servers",
        "Development team deployed code to staging environment for testing",
        "Marketing team accessed analytics dashboard to review campaign metrics",
        "Finance department ran monthly financial report generation query",
        "Customer support agent viewed user account using ticket reference",
        "System administrator reviewed audit logs for routine compliance check",
        "New employee completed mandatory security awareness training module",
        "Legal team accessed contract repository for document review",
        "Operations team monitored production metrics through internal dashboard",
        "Sales representative updated customer information in CRM system",
        "Procurement submitted purchase order for new hardware equipment",
        "HR department processed employee benefits enrollment for new hire",
        "Engineering team accessed internal wiki for technical documentation",
        "Project manager reviewed team time tracking entries for billing",
        "Database administrator performed routine index maintenance on tables",
        "Network engineer validated firewall rules during change window",
        "Security team reviewed failed login attempts from authorized devices",
        "Backup administrator verified restore functionality with test files",
        "Compliance officer generated access review report for auditors",
        "Facilities team logged maintenance request for office equipment",
        "Research team downloaded public dataset for machine learning project",
        "Training department uploaded new course materials to learning system",
        "Executive assistant scheduled meeting using corporate calendar tool",
        "Product team accessed customer feedback database to analyze reviews",
        # Additional Benign VPN examples
        "Employee connected to company VPN using authorized corporate laptop",
        "Remote worker established secure VPN tunnel with MFA authentication",
        "VPN session established from home office during approved hours",
        "User authenticated via VPN from known IP address range",
        "VPN connection logs show successful handshake with valid certificate",
        "Employee accessed internal wiki through encrypted VPN channel",
        "VPN tunnel established following standard security protocol for remote access",
        "Remote access request approved through VPN gateway with 2FA",
        "VPN connection terminated normally at end of work shift",
        "Employee reconnected to VPN after brief network interruption during meeting",
        "Help desk assisted user with VPN connection from new location",
        "VPN usage logged as part of routine security audit",
        "Remote employee accessed email through VPN as daily practice",
        "VPN connection maintained stable throughout 8-hour work session",
        "User completed VPN authentication using hardware token successfully",
    ],
    "label": [0]*25 + [1]*25 + [2]*25 + [3]*25 + [4]*40
}

df = pd.DataFrame(data)
print(f"Dataset size: {len(df)} samples")
print("\nLabel distribution:")
print(df['label'].value_counts())

# ============================================
# STEP 2: TRAIN/TEST SPLIT
# ============================================

train_texts, test_texts, train_labels, test_labels = train_test_split(
    df['text'].tolist(),
    df['label'].tolist(),
    test_size=0.2,
    random_state=42,
    stratify=df['label']
)

print(f"\nTraining samples: {len(train_texts)}")
print(f"Test samples: {len(test_texts)}")

# ============================================
# STEP 3: LOAD TOKENIZER AND MODEL
# ============================================

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)

print("\nModel and tokenizer loaded!")

# ============================================
# STEP 4: TOKENIZE DATA
# ============================================

train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=128)
test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=128)

# ============================================
# STEP 5: CREATE PYTORCH DATASET
# ============================================

class CybersecurityDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = CybersecurityDataset(train_encodings, train_labels)
test_dataset = CybersecurityDataset(test_encodings, test_labels)

# ============================================
# STEP 6: SET UP TRAINING ARGUMENTS
# ============================================

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = predictions.argmax(axis=-1)
    accuracy = accuracy_score(labels, predictions)
    return {"accuracy": accuracy}

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=8,
    warmup_steps=50,
    weight_decay=0.01,
    logging_steps=10,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)

print("\nTrainer ready!")

# ============================================
# STEP 7: TRAIN THE MODEL
# ============================================

print("\nStarting training...")
trainer.train()

# ============================================
# STEP 8: EVALUATE
# ============================================

results = trainer.evaluate()
print(f"\nTest Accuracy: {results['eval_accuracy']:.2%}")

# ============================================
# STEP 9: PREDICTION FUNCTION
# ============================================

def predict_alert(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    outputs = model(**inputs)
    prediction = outputs.logits.argmax().item()
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    confidence = probabilities.max().item()

    categories = ["Ransomware", "DDoS", "Insider Threat", "Web Attack", "Benign"]
    return categories[prediction], confidence

# ============================================
# STEP 10: TEST THE MODEL
# ============================================

test_alerts = [
    "Critical files encrypted with ransom demand for Bitcoin payment",
    "Website unreachable due to massive spike in incoming requests",
    "Employee downloading sensitive customer data before resignation",
    "SQL injection attempt detected in website login form",
    "User successfully connected to corporate VPN during office hours"
]

print("\n" + "=" * 50)
print("TESTING THE MODEL")
print("=" * 50)

for alert in test_alerts:
    category, confidence = predict_alert(alert)
    print(f"\nAlert: {alert}")
    print(f"Prediction: {category} (confidence: {confidence:.2%})")

