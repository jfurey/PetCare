CREATE TABLE IF NOT EXISTS resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    url VARCHAR(255) NOT NULL,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO resources (title, url, category, created_at) VALUES
('ASPCA Pet Care Guides', 'https://www.aspca.org/pet-care', 'Care Guides', NOW()),
('Emergency Pet Poison Hotline', 'https://www.aspca.org/pet-care/animal-poison-control', 'Emergency', NOW()),
('AKC Dog Training Resources', 'https://www.akc.org/expert-advice/training/', 'Training', NOW()),
('PetMD Nutrition Center', 'https://www.petmd.com/dog/nutrition', 'Nutrition', NOW()),
('AVMA Pet Care', 'https://www.avma.org/resources/pet-owners/petcare', 'Veterinary', NOW()),
('Local Pet Adoption Centers', 'https://www.petfinder.com', 'Adoption', NOW()),
('Pet Food Recall Alerts', 'https://www.fda.gov/animal-veterinary/safety-health/recalls-withdrawals', 'Safety', NOW()),
('Best Cat Nutrition Practices', 'https://icatcare.org/advice/cat-diet-nutrition/', 'Nutrition', NOW()),
('Bird Care Basics', 'https://www.thesprucepets.com/bird-care-and-health-4162329', 'Care Guides', NOW()),
('Fish Tank Maintenance Guide', 'https://www.thesprucepets.com/aquarium-maintenance-for-beginners-1380921', 'Care Guides', NOW());