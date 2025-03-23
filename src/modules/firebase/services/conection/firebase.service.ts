import { Injectable, OnModuleInit } from '@nestjs/common';
import * as admin from 'firebase-admin';
import * as fs from 'fs';

@Injectable()
export class FirebaseService implements OnModuleInit {
  private db: FirebaseFirestore.Firestore;

  onModuleInit() {
    if (!admin.apps.length) {
      const serviceAccount = JSON.parse(
        fs.readFileSync('src/firebase-key.json', 'utf8'),
      );

      admin.initializeApp({
        credential: admin.credential.cert(serviceAccount),
      });
    }

    this.db = admin.firestore();
  }

  async salveCrime(dados: any): Promise<string> {
    const crimesRef = this.db.collection('crimes');
    const docRef = await crimesRef.add(dados);
    return docRef.id;
  }

  async upsertCrimeRegion(colecao: string, crime: string, quantidade: number) {
    try {
      const snapshot = await this.db
        .collection(colecao)
        .where('crime', '==', crime)
        .get();

      if (!snapshot.empty) {
        snapshot.forEach(async (doc) => {
          const quantidadeAtual = parseInt(doc.data().quantidade) || 0;

          await doc.ref.update({ quantidade: quantidadeAtual + quantidade });
          console.log(
            `Atualizado: ${crime} na coleção ${colecao}, nova quantidade: ${quantidadeAtual + quantidade}`,
          );
        });
      } else {
        await this.db.collection(colecao).add({
          crime: crime,
          quantidade: quantidade,
        });
        console.log(
          `Novo crime adicionado: ${crime} na coleção ${colecao} com quantidade: ${quantidade}`,
        );
      }
    } catch (error) {
      console.log('Coleção recebida:', colecao);

      console.error('Erro ao atualizar ou criar crime:', error);
    }
  }

  async upsertCrimeBairro(colecao: string, crime: string, quantidade: number) {
    try {
      const snapshot = await this.db
        .collection(colecao)
        .where('crime', '==', crime)
        .get();

      if (!snapshot.empty) {
        snapshot.forEach(async (doc) => {
          const quantidadeAtual = parseInt(doc.data().quantidade) || 0;

          await doc.ref.update({ quantidade: quantidadeAtual + quantidade });
          console.log(
            `Atualizado: ${crime} na coleção ${colecao}, nova quantidade: ${quantidadeAtual + quantidade}`,
          );
        });
      } else {
        await this.db.collection(colecao).add({
          crime: crime,
          quantidade: quantidade,
        });
        console.log(
          `Novo crime adicionado: ${crime} na coleção ${colecao} com quantidade: ${quantidade}`,
        );
      }
    } catch (error) {
      console.log('Coleção recebida:', colecao);

      console.error('Erro ao atualizar ou criar crime:', error);
    }
  }

  async upsertCrimePorBairro(
    colecao: string,
    bairro: string,
    crime: string,
    quantidade: number,
  ) {
    try {
      const bairroRef = this.db
        .collection(colecao)
        .doc('bairros')
        .collection(bairro);

      const crimeSnapshot = await bairroRef.where('crime', '==', crime).get();

      if (!crimeSnapshot.empty) {
        crimeSnapshot.forEach(async (doc) => {
          const dadosCrime = doc.data();
          const quantidadeAtual = +dadosCrime.quantidade || 0;

          await doc.ref.update({ quantidade: quantidadeAtual + quantidade });
          console.log(
            `Atualizado: ${crime} no bairro ${bairro}, nova quantidade: ${quantidadeAtual + quantidade}`,
          );
        });
      } else {
        await bairroRef.add({ crime, quantidade });
        console.log(
          `Novo crime adicionado: ${crime} no bairro ${bairro} com quantidade: ${quantidade}`,
        );

        const bairrosDocRef = this.db.collection(colecao).doc('bairros');
        const bairrosDocSnapshot = await bairrosDocRef.get();
        if (bairrosDocSnapshot.exists) {
          const bairrosData = bairrosDocSnapshot.data()?.bairros || [];

          if (!bairrosData.includes(bairro)) {
            await bairrosDocRef.update({ bairros: [...bairrosData, bairro] });
            console.log(
              `Bairro ${bairro} adicionado ao campo "data" do documento "bairros".`,
            );
          }
        } else {
          await bairrosDocRef.set({ bairros: [bairro] }, { merge: true });
          console.log(
            `Campo "data" criado no documento "bairros" com o bairro ${bairro}.`,
          );
        }
      }
    } catch (error) {
      console.log('Coleção recebida:', colecao);
      console.log('Bairro recebido:', bairro);
      console.error('Erro ao atualizar ou criar crime no bairro:', error);
    }
  }

  async upsertCrimePorTimeSeries(
    colecao: string,
    document: string,
    date: string,
    crime: string,
    quantidade: number,
  ) {
    try {
      const bairroRef = this.db
        .collection(colecao)
        .doc(document)
        .collection(`${colecao} ${date}`);

      const crimeSnapshot = await bairroRef.where('crime', '==', crime).get();

      if (!crimeSnapshot.empty) {
        crimeSnapshot.forEach(async (doc) => {
          const dadosCrime = doc.data();
          const quantidadeAtual = +dadosCrime.quantidade || 0;

          await doc.ref.update({ quantidade: quantidadeAtual + quantidade });
          console.log(
            `Atualizado: ${crime} no bairro ${colecao}, nova quantidade: ${quantidadeAtual + quantidade}`,
          );
        });
      } else {
        await bairroRef.add({ crime, quantidade });
        console.log(
          `Novo crime adicionado: ${crime} no bairro ${colecao} com quantidade: ${quantidade}`,
        );

        const bairrosDocRef = this.db.collection(colecao).doc(document);
        const bairrosDocSnapshot = await bairrosDocRef.get();
        if (bairrosDocSnapshot.exists) {
          const bairrosData = bairrosDocSnapshot.data()?.data || [];

          if (!bairrosData.includes(date)) {
            await bairrosDocRef.update({ data: [...bairrosData, date] });
            console.log(
              `Bairro ${date} adicionado ao campo "data" do documento "bairros".`,
            );
          }
        } else {
          await bairrosDocRef.set({ data: [date] }, { merge: true });
          console.log(
            `Campo "data" criado no documento "bairros" com o bairro ${colecao}.`,
          );
        }
      }
    } catch (error) {
      console.log('Coleção recebida:', colecao);
      console.log('Bairro recebido:', colecao);
      console.error('Erro ao atualizar ou criar crime no bairro:', error);
    }
  }
}
