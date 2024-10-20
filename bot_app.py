{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1c813346-22f2-4bd7-af3a-1dca8fd5e405",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "\n",
    "#تطبيق بوت \n",
    "st.title('Trading Chatbot')\n",
    "\n",
    "# إدخال المستخدم\n",
    "user_input = st.text_input(\"أدخل استفسارك هنا:\")\n",
    "\n",
    "# دالة لإنتاج الردود (يمكن استبدالها بالنموذج المدرب)\n",
    "def generate_response(input_text):\n",
    "    # هنا يمكن أن تضيف منطق لتحليل الطلبات وتوليد ردود\n",
    "    if \"سعر\" in input_text:\n",
    "        return \"أسعار الأسهم الحالية هي: ...\"  # مثال على رد\n",
    "    else:\n",
    "        return \"آسف، لا أستطيع مساعدتك في ذلك.\"\n",
    "\n",
    "# عرض الرد عند الضغط على زر\n",
    "if st.button('احصل على رد'):\n",
    "    response = generate_response(user_input)\n",
    "    st.write(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "ae1eb5cb-9a1c-460a-9749-7aeff45bdb1d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "dad7b5c5-7b3e-4ee5-9c5f-8bd4988aa513",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
