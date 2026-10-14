# Password Generator — QA Checklist

- Test minimum and maximum supported password lengths.
- Verify selected character groups are reflected in generated output.
- Handle the case where no character group is selected.
- Confirm generation remains usable when clipboard access is denied.
- Ensure generated passwords are not logged or persisted unintentionally.
- Check that the strength label does not claim cryptographic guarantees.