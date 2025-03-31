-- Insert test users
INSERT INTO users (first_name, last_name, email, password_hash, phone) VALUES 
('John', 'Doe', 'john@example.com', '$2a$12$1234567890abcdefghijkl', '555-123-4567'),
('Mary', 'Doe', 'mary@example.com', '$2a$12$abcdefghijk1234567890l', '555-123-9876'),
('Robert', 'Johnson', 'robert@example.com', '$2a$12$qwertyuiopasdfghjklzxc', '555-456-7890'),
('Lisa', 'Johnson', 'lisa@example.com', '$2a$12$zxcvbnmasdfghjklqwertyu', '555-456-7891'),
('Michael', 'Wilson', 'michael@example.com', '$2a$12$poiuytrewqlkjhgfdsamnbv', '555-234-5678'),
('Emma', 'Clark', 'emma@example.com', '$2a$12$lkjhgfdsazxcvbnmqwertyui', '555-876-5432'),
('David', 'Miller', 'david@example.com', '$2a$12$mnbvcxzasdfghjklpoiuytre', '555-345-6789');

-- Insert test pets
INSERT INTO pets (name, species, breed, age, weight, gender, profile_picture) VALUES 
('Max', 'Dog', 'Golden Retriever', 3, 65.5, 'Male', 'max_profile.jpg'),
('Bella', 'Dog', 'Labrador', 2, 55.3, 'Female', 'bella_profile.jpg'),
('Oliver', 'Bird', 'Cockatiel', 4, 0.2, 'Male', 'oliver_profile.jpg'),
('Luna', 'Cat', 'Maine Coon', 3, 12.5, 'Female', 'luna_profile.jpg'),
('Bubbles', 'Fish', 'Goldfish', 1, 0.1, 'Unknown', 'bubbles_profile.jpg');

-- Connect users to pets (ownership)
INSERT INTO pet_ownership (pet_id, user_id, role) VALUES 
(1, 1, 'Primary'),   -- John Doe is primary owner of Max
(1, 2, 'Secondary'), -- Mary Doe (John's wife) is secondary owner of Max
(2, 3, 'Primary'),   -- Robert Johnson is primary owner of Bella
(2, 4, 'Secondary'), -- Lisa Johnson (Robert's wife) is secondary owner of Bella
(3, 5, 'Primary'),   -- Michael Wilson is primary owner of Oliver (single pet owner)
(4, 6, 'Primary'),   -- Emma Clark is primary owner of Luna (single pet owner)
(5, 7, 'Primary');   -- David Miller is primary owner of Charlie (single pet owner)

-- Insert test contacts
INSERT INTO contacts (contact_type, name, company_name, phone, email, address) VALUES 
('Veterinarian', 'Dr. Sarah Williams', 'Healthy Pets Clinic', '555-111-2222', 'dr.williams@healthypets.com', '123 Vet Street, Anytown, USA'),
('Groomer', 'Alex Johnson', 'Furry Friends Grooming', '555-333-4444', 'alex@furryfriends.com', '456 Groom Ave, Anytown, USA'),
('Trainer', 'Sam Thompson', 'Obedient Paws Training', '555-555-6666', 'sam@obedientpaws.com', '789 Tr