import pickle
import streamlit as st

st.set_page_config(layout="wide")


# loading the saved models

skin_disorder_classification_model = pickle.load(open('skin_disorder_classification_model.pkl', 'rb'))
  
# page title
st.title('Skin Disorder Classification ML Model')

st.markdown(""" The differential diagnosis of erythemato-squamous diseases is a real problem in dermatology. They all share the clinical features of erythema and scaling, with very little differences.""") 

st.markdown("""The diseases in this group are:""")

data = [
    {"name": "psoriasis", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Psoriasis_on_back1.jpg/300px-Psoriasis_on_back1.jpg"},
    {"name": "seboreic dermatitis", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Sequeira_Plate_18.jpg/300px-Sequeira_Plate_18.jpg"},
    {"name": "lichen planus", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Lichen_Planus_%282%29.JPG/300px-Lichen_Planus_%282%29.JPG"},
    {"name": "pityriasis rosea", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Pityriasisrosa.png/300px-Pityriasisrosa.png"},
    {"name": "cronic dermatitis", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Dermatitis2015.jpg/300px-Dermatitis2015.jpg"},
    {"name": "pityriasis rubra pilaris", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Plate_XXXIII%2C_Pityriasis_rubra_pilaris%2C_Crocker_1896_Wellcome_L0074323.jpg/300px-Plate_XXXIII%2C_Pityriasis_rubra_pilaris%2C_Crocker_1896_Wellcome_L0074323.jpg"},
]

for entry in data:
    st.write(f"[{entry['name']}]({entry['image_url']})")

st.markdown("""Usually a biopsy is necessary for the diagnosis but unfortunately these diseases share many histopathological features as well. Another difficulty for the differential diagnosis is that a disease may show the features of another disease at the beginning stage and may have the characteristic features at the following stages. Patients were first evaluated clinically with 12 features. Afterwards, skin samples were taken for the evaluation of 22 histopathological features. The values of the histopathological features are determined by an analysis of the samples under a microscope.

**Clinical Attributes:**
- Erythema - A skin reaction that can be triggered by an infection or some medicines.
- Scaling - The loss of the outer layer of the epidermis in large, scale-like flakes
- Definite Borders -  Border description of skin lesions, i.e, areas of skin that are different from the skin around them.
- itching - Of, relating to, or characterized by an irritating sensation of the skin.
- Koebner Phenomenon - Also called the Koebner response or the isomorphic response, is the appearance of skin lesions on lines of trauma
- Polygonal Papules - A papule is a small, well-defined bump in the skin. It may have a rounded, pointed or flat top.
- Follicular Papules - Individual papules that include a central hair follicle.
- Oral mucosal involvement - Oral involvement generally consists of mucosal ulceration associated with lesions of the underlying bone.
- Knee and elbow involvement - Skin complexities on knee and elbow
- Scalp involvement - Skin complexities on scalp
- Family history - If any of these diseases has been observed in the family.
- Age of the person

**Histopathological Attributes:**
- Melanin_incontinence - Pigmentary incontinence, which is a phenomenon observed in some inflammatory skin disorders. Clinically it may be seen as a slate-colored pigmentation. Histologically it is seen as an accumulation of melanin in the upper dermis.
- Eosinophils in the infiltrate - Eosinophils are a kind of white blood cell that helps fight disease. Eosinophil infiltration is a common finding in a broad spectrum of skin diseases, despite the fact that the skin is devoid of eosinophils under physiologic conditions.
- PNL infiltrate - Pure Neuritic Leprosy(PNL) Infiltrate.
- Fibrosis of the papillary dermis - Overgrowth, hardening, and/or scarring of various tissues and excess deposition of extracellular matrix components including collagen in the thin top layer of the dermis (the inner layer of the skin), i.e, papillary dermis.
- Exocytosis - Exocytosis is infiltration of the epidermis by inflammatory or circulating blood cells. Pathological changes may arise in epidermis, dermis and/or subcutaneous tissue (tissues under the skin).
- Acanthosis - A skin condition that causes a dark discoloration in body folds and creases. It typically affects the armpits, groin and neck.
- Hyperkeratosis - The increased thickness of the stratum corneum, the outer layer of the skin. Stratum corneum is composed of multiple layers of keratinocyte bodies that, during maturation, produced keratin and subsequently have lost their nucleus and - cytoplasmic organelles.
- Parakeratosis - Incomplete maturation of epidermal keratinocytes, resulting in abnormal retention of nuclei in the stratum corneum. It occurs in many diseases of the skin, particularly in psoriasis.
- Clubbing of the rete ridges - Rete ridges are the epithelial extensions that project into the underlying connective tissue in both skin and mucous membranes.
- Elongation of the rete ridges - Mechanical stretching stimulates growth of the basal layer and rete ridges in the epidermis.
- Thinning_of_the_suprapapillary_epidermis - A thinning of the granular layer at the tips of the papillae.
- Spongiform_pustule - Pustular psoriasis which is microscopically manifested as characteristic spongiform pustule.
- Munro_microabcess - One of the characteristic histological features of early psoriasis vulgaris
- Focal_hypergranulosis An increased thickness of the stratum granulosum.
- Disappearance_of_the_granular_layer - Degeneration of granular layer in Cerebellum.
- Vacuolisation_and_damage_of_basal_layer - presence of vacuolisation and damage of skin basal layer.
- Spongiosis - presence of intercellular edema.
- Saw-tooth_appearance_of_retes - appearance of saw tooth patterns under the skin tissue.
- Follicular_horn_plug - presence of follicular horn plugs
- Perifollicular_parakeratosis - keratinization characterized by the retention of nuclei in tissues surrounding skin follicles.
- Inflammatory_monoluclear_inflitrate - increase in the number of infiltrating mononuclear cells in the skin.
- Band-like_infiltrate - basal epidermis in a banded pattern.
        
""")
       
# getting the input data from the user  
  
st.markdown('Fill the below information from the clinical test to check the type of skin disorder:')

col1, col2, col3 = st.columns(3)
    
with col1:
    erythema = st.radio("Erythema", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if erythema == 'Not present':
        erythema = 0
    elif erythema == 'Low or mild presence':
        erythema = 1
    elif erythema == 'Moderate presence':
        erythema = 2
    else:
        erythema = 3


with col2:
    scaling = st.radio("Scaling", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])

    if scaling == 'Not present':
        scaling = 0
    elif scaling == 'Low or mild presence':
        scaling = 1
    elif scaling == 'Moderate presence':
        scaling = 2
    else:
        scaling = 3


with col3:
    definite_borders = st.radio("Definite_borders", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    if definite_borders == 'Not present':
        definite_borders = 0
    elif definite_borders == 'Low or mild presence':
        definite_borders = 1
    elif definite_borders == 'Moderate presence':
        definite_borders = 2
    else:
        definite_borders = 3


with col1:
    itching = st.radio("Itching", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])

    if itching == 'Not present':
        itching = 0
    elif itching == 'Low or mild presence':
        itching = 1
    elif itching == 'Moderate presence':
        itching = 2
    else:
        itching = 3


with col2:
    koebner_phenomenon = st.radio("Koebner_phenomenon", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    if koebner_phenomenon == 'Not present':
        koebner_phenomenon = 0
    elif koebner_phenomenon == 'Low or mild presence':
        koebner_phenomenon = 1
    elif koebner_phenomenon == 'Moderate presence':
        koebner_phenomenon = 2
    else:
        koebner_phenomenon = 3


with col3:
    polygonal_papules = st.radio("Polygonal_papules", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if polygonal_papules == 'Not present':
        polygonal_papules = 0
    elif polygonal_papules == 'Low or mild presence':
        polygonal_papules = 1
    elif polygonal_papules == 'Moderate presence':
        polygonal_papules = 2
    else:
        polygonal_papules = 3
    

with col1:
    follicular_papules = st.radio("Follicular_papules", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if follicular_papules == 'Not present':
        follicular_papules = 0
    elif follicular_papules == 'Low or mild presence':
        follicular_papules = 1
    elif follicular_papules == 'Moderate presence':
        follicular_papules = 2
    else:
        follicular_papules = 3
    

with col2:
    oral_mucosal_involvement = st.radio("Oral_mucosal_involvement", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if oral_mucosal_involvement == 'Not present':
        oral_mucosal_involvement = 0
    elif oral_mucosal_involvement == 'Low or mild presence':
        oral_mucosal_involvement = 1
    elif oral_mucosal_involvement == 'Moderate presence':
        oral_mucosal_involvement = 2
    else:
        oral_mucosal_involvement = 3


with col3:
    knee_and_elbow_involvement = st.radio("Knee_and_elbow_involvement", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if knee_and_elbow_involvement == 'Not present':
        knee_and_elbow_involvement = 0
    elif knee_and_elbow_involvement == 'Low or mild presence':
        knee_and_elbow_involvement = 1
    elif knee_and_elbow_involvement == 'Moderate presence':
        knee_and_elbow_involvement = 2
    else:
        knee_and_elbow_involvement = 3


with col1:
    scalp_involvement = st.radio("Scalp_involvement", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if scalp_involvement == 'Not present':
        scalp_involvement = 0
    elif scalp_involvement == 'Low or mild presence':
        scalp_involvement = 1
    elif scalp_involvement == 'Moderate presence':
        scalp_involvement = 2
    else:
        scalp_involvement = 3
    

with col2:
    melanin_incontinence = st.radio("Melanin_incontinence", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if melanin_incontinence == 'Not present':
        melanin_incontinence = 0
    elif melanin_incontinence == 'Low or mild presence':
        melanin_incontinence = 1
    elif melanin_incontinence == 'Moderate presence':
        melanin_incontinence = 2
    else:
        melanin_incontinence = 3


with col3:
    eosinophils_in_the_infiltrate = st.radio("Eosinophils_in_the_infiltrate", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if eosinophils_in_the_infiltrate == 'Not present':
        eosinophils_in_the_infiltrate = 0
    elif eosinophils_in_the_infiltrate == 'Low or mild presence':
        eosinophils_in_the_infiltrate = 1
    elif eosinophils_in_the_infiltrate == 'Moderate presence':
        eosinophils_in_the_infiltrate = 2
    else:
        eosinophils_in_the_infiltrate = 3


with col1:
    PNL_infiltrate = st.radio("PNL_infiltrate", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if PNL_infiltrate == 'Not present':
        PNL_infiltrate = 0
    elif PNL_infiltrate == 'Low or mild presence':
        PNL_infiltrate = 1
    elif PNL_infiltrate == 'Moderate presence':
        PNL_infiltrate = 2
    else:
        PNL_infiltrate = 3
   

with col2:
    fibrosis_of_the_papillary_dermis = st.radio("Fibrosis_of_the_papillary_dermis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if fibrosis_of_the_papillary_dermis == 'Not present':
        fibrosis_of_the_papillary_dermis = 0
    elif fibrosis_of_the_papillary_dermis == 'Low or mild presence':
        fibrosis_of_the_papillary_dermis = 1
    elif fibrosis_of_the_papillary_dermis == 'Moderate presence':
        fibrosis_of_the_papillary_dermis = 2
    else:
        fibrosis_of_the_papillary_dermis = 3
 

with col3:
    exocytosis = st.radio("Exocytosis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if exocytosis == 'Not present':
        exocytosis = 0
    elif exocytosis == 'Low or mild presence':
        exocytosis = 1
    elif exocytosis == 'Moderate presence':
        exocytosis = 2
    else:
        exocytosis = 3


with col1:
    acanthosis = st.radio("Acanthosis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if acanthosis == 'Not present':
        acanthosis = 0
    elif acanthosis == 'Low or mild presence':
        acanthosis = 1
    elif acanthosis == 'Moderate presence':
        acanthosis = 2
    else:
        acanthosis = 3
    

with col2:
    hyperkeratosis = st.radio("Hyperkeratosis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if hyperkeratosis == 'Not present':
        hyperkeratosis = 0
    elif hyperkeratosis == 'Low or mild presence':
        hyperkeratosis = 1
    elif hyperkeratosis == 'Moderate presence':
        hyperkeratosis = 2
    else:
        hyperkeratosis = 3
    

with col3:
    parakeratosis = st.radio("Parakeratosis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if parakeratosis == 'Not present':
        parakeratosis = 0
    elif parakeratosis == 'Low or mild presence':
        parakeratosis = 1
    elif parakeratosis == 'Moderate presence':
        parakeratosis = 2
    else:
        parakeratosis = 3
 

with col1:
    clubbing_of_the_rete_ridges = st.radio("Clubbing_of_the_rete_ridges", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if clubbing_of_the_rete_ridges == 'Not present':
        clubbing_of_the_rete_ridges = 0
    elif clubbing_of_the_rete_ridges == 'Low or mild presence':
        clubbing_of_the_rete_ridges = 1
    elif clubbing_of_the_rete_ridges == 'Moderate presence':
        clubbing_of_the_rete_ridges = 2
    else:
        clubbing_of_the_rete_ridges = 3
 

with col2:
    elongation_of_the_rete_ridges = st.radio("Elongation_of_the_rete_ridges", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if elongation_of_the_rete_ridges == 'Not present':
        elongation_of_the_rete_ridges = 0
    elif elongation_of_the_rete_ridges == 'Low or mild presence':
        elongation_of_the_rete_ridges = 1
    elif elongation_of_the_rete_ridges == 'Moderate presence':
        elongation_of_the_rete_ridges = 2
    else:
        elongation_of_the_rete_ridges = 3


with col3:
    thinning_of_the_suprapapillary_epidermis = st.radio("Thinning_of_the_suprapapillary_epidermis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if thinning_of_the_suprapapillary_epidermis == 'Not present':
        thinning_of_the_suprapapillary_epidermis = 0
    elif thinning_of_the_suprapapillary_epidermis == 'Low or mild presence':
        thinning_of_the_suprapapillary_epidermis = 1
    elif thinning_of_the_suprapapillary_epidermis == 'Moderate presence':
        thinning_of_the_suprapapillary_epidermis = 2
    else:
        thinning_of_the_suprapapillary_epidermis = 3


with col1:
    spongiform_pustule = st.radio("Spongiform_pustule", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if spongiform_pustule == 'Not present':
        spongiform_pustule = 0
    elif spongiform_pustule == 'Low or mild presence':
        spongiform_pustule = 1
    elif spongiform_pustule == 'Moderate presence':
        spongiform_pustule = 2
    else:
        spongiform_pustule = 3


with col2:
    munro_microabcess = st.radio("Munro_microabcess", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if munro_microabcess == 'Not present':
        munro_microabcess = 0
    elif munro_microabcess == 'Low or mild presence':
        munro_microabcess = 1
    elif munro_microabcess == 'Moderate presence':
        munro_microabcess = 2
    else:
        munro_microabcess = 3
    

with col3:
    focal_hypergranulosis = st.radio("Focal_hypergranulosis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if focal_hypergranulosis == 'Not present':
        focal_hypergranulosis = 0
    elif focal_hypergranulosis == 'Low or mild presence':
        focal_hypergranulosis = 1
    elif focal_hypergranulosis == 'Moderate presence':
        focal_hypergranulosis = 2
    else:
        focal_hypergranulosis = 3


with col1:
    disappearance_of_the_granular_layer = st.radio("Disappearance_of_the_granular_layer", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if disappearance_of_the_granular_layer == 'Not present':
        disappearance_of_the_granular_layer = 0
    elif disappearance_of_the_granular_layer == 'Low or mild presence':
        disappearance_of_the_granular_layer = 1
    elif disappearance_of_the_granular_layer == 'Moderate presence':
        disappearance_of_the_granular_layer = 2
    else:
        disappearance_of_the_granular_layer = 3


with col2:
    vacuolisation_and_damage_of_basal_layer = st.radio("Vacuolisation_and_damage_of_basal_layer", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if vacuolisation_and_damage_of_basal_layer == 'Not present':
        vacuolisation_and_damage_of_basal_layer = 0
    elif vacuolisation_and_damage_of_basal_layer == 'Low or mild presence':
        vacuolisation_and_damage_of_basal_layer = 1
    elif vacuolisation_and_damage_of_basal_layer == 'Moderate presence':
        vacuolisation_and_damage_of_basal_layer = 2
    else:
        vacuolisation_and_damage_of_basal_layer = 3
    

with col3:
    spongiosis = st.radio("Spongiosis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if spongiosis == 'Not present':
        spongiosis = 0
    elif spongiosis == 'Low or mild presence':
        spongiosis = 1
    elif spongiosis == 'Moderate presence':
        spongiosis = 2
    else:
        spongiosis = 3
 

with col1:
    saw_tooth_appearance_of_retes = st.radio("Saw_tooth_appearance_of_retes", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if saw_tooth_appearance_of_retes == 'Not present':
        saw_tooth_appearance_of_retes = 0
    elif saw_tooth_appearance_of_retes == 'Low or mild presence':
        saw_tooth_appearance_of_retes = 1
    elif saw_tooth_appearance_of_retes == 'Moderate presence':
        saw_tooth_appearance_of_retes = 2
    else:
        saw_tooth_appearance_of_retes = 3
 

with col2:
    follicular_horn_plug = st.radio("Follicular_horn_plug", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if follicular_horn_plug == 'Not present':
        follicular_horn_plug = 0
    elif follicular_horn_plug == 'Low or mild presence':
        follicular_horn_plug = 1
    elif follicular_horn_plug == 'Moderate presence':
        follicular_horn_plug = 2
    else:
        follicular_horn_plug = 3
    

with col3:
    perifollicular_parakeratosis = st.radio("Perifollicular_parakeratosis", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if perifollicular_parakeratosis == 'Not present':
        perifollicular_parakeratosis = 0
    elif perifollicular_parakeratosis == 'Low or mild presence':
        perifollicular_parakeratosis = 1
    elif perifollicular_parakeratosis == 'Moderate presence':
        perifollicular_parakeratosis = 2
    else:
        perifollicular_parakeratosis = 3


with col1:
    inflammatory_monoluclear_inflitrate = st.radio("Inflammatory_monoluclear_inflitrate", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if inflammatory_monoluclear_inflitrate == 'Not present':
        inflammatory_monoluclear_inflitrate = 0
    elif inflammatory_monoluclear_inflitrate == 'Low or mild presence':
        inflammatory_monoluclear_inflitrate = 1
    elif inflammatory_monoluclear_inflitrate == 'Moderate presence':
        inflammatory_monoluclear_inflitrate = 2
    else:
        inflammatory_monoluclear_inflitrate = 3


with col2:
    band_like_infiltrate = st.radio("Band_like_infiltrate", ["Not present", "Low or mild presence", "Moderate presence", "Largest amount possible"])
    
    if band_like_infiltrate == 'Not present':
        band_like_infiltrate = 0
    elif band_like_infiltrate == 'Low or mild presence':
        band_like_infiltrate = 1
    elif band_like_infiltrate == 'Moderate presence':
        band_like_infiltrate = 2
    else:
        band_like_infiltrate = 3  
  

with col3:
    family_history =st.radio("Family_history", ["Not present", "Present"])

if family_history == 'Present':
    family_history_Not_Observed = 0
    family_history_Observed = 1
else:
    family_history_Not_Observed = 1
    family_history_Observed = 0


with col1:
    Age = st.slider('Age of the Person')
    


 # creating a button for Prediction
     
if st.button('Skin Disorder'):
  
    prediction = skin_disorder_classification_model.predict([[erythema,scaling,definite_borders,itching,koebner_phenomenon,polygonal_papules,follicular_papules,oral_mucosal_involvement,knee_and_elbow_involvement,scalp_involvement,melanin_incontinence,eosinophils_in_the_infiltrate,PNL_infiltrate,fibrosis_of_the_papillary_dermis,exocytosis,acanthosis,hyperkeratosis,parakeratosis,clubbing_of_the_rete_ridges,elongation_of_the_rete_ridges,thinning_of_the_suprapapillary_epidermis,spongiform_pustule,munro_microabcess,focal_hypergranulosis,disappearance_of_the_granular_layer,vacuolisation_and_damage_of_basal_layer,spongiosis,saw_tooth_appearance_of_retes,follicular_horn_plug,perifollicular_parakeratosis,inflammatory_monoluclear_inflitrate,band_like_infiltrate,Age,family_history_Not_Observed,family_history_Observed]])

    st.write("Skin Disorder Result:", prediction[0])

