-- Add a new pet
INSERT INTO pets (name, species, breed, age, weight, gender, profile_picture) 
VALUES ('Buddy', 'Dog', 'Beagle', 2, 25.5, 'Male', 'buddy_profile.jpg');

-- Make John the primary owner and Mary the secondary owner
INSERT INTO pet_ownership (pet_id, user_id, role) 
VALUES (6, 1, 'Primary'), (6, 2, 'Secondary');